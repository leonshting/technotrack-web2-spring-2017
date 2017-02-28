from django.apps import AppConfig


class AwardsConfig(AppConfig):
    name = 'awards'

    def ready(self):
        from . import signals
