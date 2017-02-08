from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    blacklisted = models.ManyToManyField('self', related_name='foes', symmetrical=False, through='socnet.Blacklist')
    friends = models.ManyToManyField('self', symmetrical=False, through='socnet.Friend')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
