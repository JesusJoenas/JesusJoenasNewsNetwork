from django.apps import AppConfig

class PngAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'png_app'

    # This will automatically connect the signals when the app is ready
    def ready(self):
        import png_app.signals
