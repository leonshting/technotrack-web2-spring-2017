from django.apps import AppConfig


class FeedConfig(AppConfig):
    name = 'feed'

    def ready(self):
        from . import signals
