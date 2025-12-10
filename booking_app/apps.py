from django.apps import AppConfig


class BookingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_app'

    def ready(self):
        """
        Auto-create a default superuser on first run in environments
        where we can't access manage.py createsuperuser (like Render free tier).
        """
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        User = get_user_model()

        try:
            # Only create if no superuser exists
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username='leonadmin',
                    email='leonfreeman6@gmail.com',
                    password='Project3Admin!'
                )
        except (OperationalError, ProgrammingError):
            # This happens during initial migrations before auth tables exist – ignore.
            pass
