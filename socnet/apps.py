from django.apps import AppConfig


class SocnetConfig(AppConfig):
    name = 'socnet'

    def ready(self):
        from . import signals
        from . import api