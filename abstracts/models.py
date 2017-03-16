from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.conf import settings


class AuthoredMixin(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class CreatedMixin(models.Model):

    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def save(self, **kwargs):
        now = timezone.now()
        if not self.pk:
            self.date_added = now

        self.date_modified = now

        super(CreatedMixin, self).save()

    class Meta:
        abstract = True


class GenericRelatedMixin(models.Model):

    content_type = models.ForeignKey(ContentType, related_name='%(app_label)s_%(class)s_content_type')
    object = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object')

    class Meta:
        abstract = True