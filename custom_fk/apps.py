from django.apps import AppConfig


class CustomFkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_fk'
