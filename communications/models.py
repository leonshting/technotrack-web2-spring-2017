from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from abstracts.models import AuthoredMixin, CreatedMixin


class Chat(AuthoredMixin, CreatedMixin):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants')
    def __str__(self):
        return 'Chat authored by {}'.format(self.author)


class Message(AuthoredMixin, CreatedMixin):
    content = models.TextField()
    chat = models.ForeignKey(Chat)

    def __str__(self):
        return 'Message authored by {}'.format(self.author)

