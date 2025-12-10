from django.apps import AppConfig


class BookingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_app'

    def ready(self):
        """
        - Auto-create a default superuser (for Render free tier).
        - Auto-create default Tables and Menu Items if none exist.
        This runs on startup in production; database errors during
        initial migrations are safely ignored.
        """
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        try:
            # Import here to avoid circular imports at module level
            from .models import Table, MenuItem
        except Exception:
            # Models may not be ready on some operations – just skip
            return

        User = get_user_model()

        try:
            # 1) Ensure there is at least one superuser
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username='leonadmin',
                    email='leonfreeman6@gmail.com',
                    password='Project3Admin!'
                )

            # 2) Seed default tables if none exist
            if not Table.objects.exists():
                default_tables = [
                    ("Window Table", 2),
                    ("Corner Booth", 4),
                    ("Family Table", 6),
                    ("High Bar Table", 2),
                ]
                for name, capacity in default_tables:
                    Table.objects.create(name=name, capacity=capacity)

            # 3) Seed default menu items if none exist
            if not MenuItem.objects.exists():
                default_menu = [
                    ("Espresso", "Rich single-shot espresso.", 2.50),
                    ("Flat White", "Smooth blend of espresso and velvety steamed milk.", 3.20),
                    ("Vanilla Latte", "Espresso with steamed milk and vanilla syrup.", 3.80),
                    ("Mocha", "Chocolate, espresso and steamed milk with whipped cream.", 3.95),
                    ("House Filter Coffee", "Bottomless freshly brewed filter coffee.", 2.20),
                    ("Croissant", "Buttery flaky croissant, baked fresh daily.", 2.40),
                    ("Chocolate Brownie", "Fudgy chocolate brownie with walnut pieces.", 2.80),
                    ("Avocado Toast", "Sourdough toast topped with smashed avocado and chilli flakes.", 5.50),
                ]
                for name, description, price in default_menu:
                    MenuItem.objects.create(
                        name=name,
                        description=description,
                        price=price
                    )

        except (OperationalError, ProgrammingError):
            # Happens during migrate / before tables exist – safe to ignore
            pass
