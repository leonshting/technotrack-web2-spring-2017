from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
