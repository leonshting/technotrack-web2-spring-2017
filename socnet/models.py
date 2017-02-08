from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from core.models import User
# Create your models here.


class Authored:
    author = models.ForeignKey(SocialUser)

    class Meta:
        abstract = True


class Created:
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SocialUser(User):
    """
        without Created inheritance, date_joined instead
    """
    blacklist = models.ManyToManyField('self')
    friends = models.ManyToManyField('self')


class Friendship(models.Model, Created, Authored):
    recipient = models.ForeignKey(SocialUser)
    approved = models.BooleanField()



class Chat(models.Model, Authored, Created):
    users = models.ManyToManyField(SocialUser)


class Message(models.Model, Authored, Created):
    content = models.TextField()
    chat = models.ForeignKey(Chat)


class Like(models.Model, Authored, Created):
    content_type = models.ForeignKey(ContentType)
    object = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object')

