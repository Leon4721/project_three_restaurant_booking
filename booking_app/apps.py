from django.apps import AppConfig


class BookingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "booking_app"

    def ready(self):
        """
        Seeds default tables and menu items safely.

        Note:
        We DO NOT create a superuser here, to avoid storing any
        passwords or secrets in the repository. The admin user
        should be created manually using `createsuperuser`.
        """
        from django.db.utils import OperationalError, ProgrammingError

        try:
            from .models import Table, MenuItem
        except Exception:
           
            return

        try:
           
            if not Table.objects.exists():
                default_tables = [
                    ("Window Table", 2),
                    ("Corner Booth", 4),
                    ("Family Table", 6),
                    ("High Bar Table", 2),
                ]
                for name, capacity in default_tables:
                    Table.objects.create(name=name, capacity=capacity)

          
            if not MenuItem.objects.exists():
                default_menu = [
                    (
                        "Single Origin Ethiopia",
                        "Light roast with notes of jasmine, bergamot and citrus. "
                        "Washed process from Yirgacheffe.",
                        3.80,
                    ),
                    (
                        "Kenyan AA Pour Over",
                        "Bright, juicy cup with blackcurrant and grapefruit acidity. "
                        "Brewed to order as V60.",
                        4.20,
                    ),
                    (
                        "Colombian House Espresso",
                        "Our signature double shot blend with dark chocolate, caramel "
                        "and roasted almond.",
                        2.80,
                    ),
                    (
                        "Tokyo Matcha Latte",
                        "Ceremonial grade Japanese matcha whisked with micro-foamed milk, "
                        "naturally sweet and vibrant.",
                        4.50,
                    ),
                ]
                for name, description, price in default_menu:
                    MenuItem.objects.create(
                        name=name,
                        description=description,
                        price=price,
                    )

        except (OperationalError, ProgrammingError):
            # Database might not be ready during migrate, etc.
            pass
