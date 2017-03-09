from __future__ import unicode_literals


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    friends = models.ManyToManyField('self', symmetrical=False, through='socnet.Friend')
    friends_count = models.IntegerField(default=0)
    blacklisted = models.ManyToManyField('self',
                                         related_name='foes',
                                         symmetrical=False,
                                         through='socnet.Blacklist',
                                         through_fields=['foofoe', 'barfoe']
                                         )
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
