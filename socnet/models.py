import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from core.models import User
# Create your models here.


class AuthoredMixin(models.Model):
    author = models.ForeignKey('core.User')

    class Meta:
        abstract = True


class CreatedMixin(models.Model):
    date_added = models.DateTimeField(default=datetime.datetime.now)
    date_modified = models.DateTimeField()

    def save(self):
        self.date_modified = datetime.datetime.now()
        super(CreatedMixin, self).save()

    class Meta:
        abstract = True


class Friendship(CreatedMixin, AuthoredMixin):
    recipient = models.ForeignKey('core.User', related_name='recipient')
    approved = models.BooleanField()


class Friend(CreatedMixin):
    foofriend = models.ForeignKey('core.User', related_name='foofriend')
    barfriend = models.ForeignKey('core.User', related_name='barfriend')


class Blacklist(CreatedMixin):
    foofoe = models.ForeignKey('core.User', related_name='foofoe')
    barfoe = models.ForeignKey('core.User', related_name='barfoe')


class Chat(AuthoredMixin, CreatedMixin):
    users = models.ManyToManyField('core.User', related_name='participants')


class Message(AuthoredMixin, CreatedMixin):
    content = models.TextField()
    chat = models.ForeignKey(Chat)


class Like(AuthoredMixin, CreatedMixin):
    content_type = models.ForeignKey(ContentType)
    object = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object')


class Event(AuthoredMixin, CreatedMixin):
    content_type = models.ForeignKey(ContentType)
    object = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object')