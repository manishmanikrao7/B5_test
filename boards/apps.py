from django.apps import AppConfig
# added a new line

class BoardsConfig(AppConfig):
    """this is a boards config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boards'
