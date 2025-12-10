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
                       # 3) Seed default menu items if none exist
            if not MenuItem.objects.exists():
                default_menu = [
                    (
                        "Single Origin Ethiopia",
                        "Light roast with notes of jasmine, bergamot and citrus. Washed process from Yirgacheffe.",
                        3.80
                    ),
                    (
                        "Kenyan AA Pour Over",
                        "Bright, juicy cup with blackcurrant and grapefruit acidity. Brewed to order as V60.",
                        4.20
                    ),
                    (
                        "Colombian House Espresso",
                        "Our signature double shot blend with dark chocolate, caramel and roasted almond.",
                        2.80
                    ),
                    (
                        "Tokyo Matcha Latte",
                        "Ceremonial grade Japanese matcha whisked with micro-foamed milk, naturally sweet and vibrant.",
                        4.50
                    ),
                    (
                        "New York Cold Brew",
                        "24-hour cold-steeped coffee served over ice, smooth and low in acidity.",
                        4.00
                    ),
                    (
                        "Spanish Latte",
                        "Espresso with steamed milk and a hint of condensed milk for a silky, caramel sweetness.",
                        3.95
                    ),
                    (
                        "Chai from Mumbai",
                        "Masala chai infused with cardamom, ginger and cloves, served latte-style.",
                        3.60
                    ),
                    (
                        "Parisian Butter Croissant",
                        "All-butter croissant made with French flour, laminated for extra layers and crunch.",
                        2.80
                    ),
                    (
                        "Lisbon Pastel de Nata",
                        "Traditional Portuguese custard tart with caramelised top and flaky pastry shell.",
                        2.60
                    ),
                    (
                        "Brooklyn Chocolate Cookie",
                        "Soft-baked dark chocolate cookie with sea salt and chunky chips.",
                        2.50
                    ),
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
