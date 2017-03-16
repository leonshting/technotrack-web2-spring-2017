from django.apps import AppConfig


class CommunicationsConfig(AppConfig):
    name = 'communications'

    def ready(self):
        from . import api
