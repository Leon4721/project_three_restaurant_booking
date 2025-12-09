from django.db import models
import uuid
from django.core.exceptions import ValidationError


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (seats {self.capacity})"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - £{self.price}"


class Booking(models.Model):
    booking_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time', 'table')
        ordering = ['date', 'time']

    def clean(self):
        if self.guests > self.table.capacity:
            raise ValidationError(
                {"guests": f"Table {self.table.name} can only seat {self.table.capacity} guests."}
            )

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
