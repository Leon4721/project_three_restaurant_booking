from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid


class Table(models.Model):
    """
    Physical tables inside the café.
    """
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()

    LOCATION_CHOICES = [
        ("WINDOW", "Window"),
        ("CENTRAL", "Central floor"),
        ("CORNER", "Corner booth"),
        ("OUTSIDE", "Outside"),
    ]
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default="CENTRAL",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Use this to disable a table without deleting it.",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} (seats {self.capacity})"


class MenuItem(models.Model):
    """
    Simple menu model – used to display sample items on the site.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - £{self.price}"


class Booking(models.Model):
    """
    Customer booking for a particular date/time and table.
    Includes a booking code for the user to manage/cancel their booking.
    """
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
    ]

    booking_code = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        help_text="Code used by customer to manage / cancel booking.",
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        related_name="bookings",
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    special_requests = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-time"]
        constraints = [
            models.UniqueConstraint(
                fields=["table", "date", "time"],
                name="unique_table_timeslot",
            )
        ]

    def clean(self):
        """
        Extra validation to make sure we don't book more guests
        than the table can hold.
        """
        if self.table and self.guests > self.table.capacity:
            raise ValidationError(
                {
                    "guests": (
                        f"Table {self.table.name} can only seat "
                        f"{self.table.capacity} guests."
                    )
                }
            )

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time} ({self.booking_code})"

    def save(self, *args, **kwargs):
        """
        Generate a shorter, user-friendly booking code on first save.
        """
        if not self.booking_code:
            self.booking_code = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)
