#coding = utf-8

from django.db import models
from abstracts.models import CreatedMixin, AuthoredMixin
from django.contrib.contenttypes.models import ContentType

from django.conf import settings

from feed.models import EventableMixin


class Friendship(CreatedMixin, AuthoredMixin, EventableMixin):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipient')
    approved = models.BooleanField()

    def __str__(self):
        return "friendship bw {} and {}".format(self.recipient, self.author)


class Friend(CreatedMixin):
    foofriend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='foofriend')
    barfriend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='barfriend')
    friendship = models.ForeignKey(Friendship, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "friendship bw {} and {}".format(self.foofriend, self.barfriend)

    class Meta:
        unique_together = ['foofriend', 'barfriend']


class Blacklist(AuthoredMixin, CreatedMixin, EventableMixin):
    foofoe = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='foofoe')
    barfoe = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='barfoe')

    def __str__(self):
        return "blacklisted by {} to {}".format(self.foofoe, self.barfoe)

