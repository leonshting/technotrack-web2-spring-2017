from django.db import models
from django.utils import timezone
from django.conf import settings



class AuthoredMixin(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class CreatedMixin(models.Model):

    #date_added = models.DateTimeField(default=datetime.datetime.now)  # auto_now_add=True
    #date_modified = models.DateTimeField(default=datetime.datetime.now)  # auto_now=True

    def save(self, **kwargs):
        now = timezone.now()
        if not self.pk:
            self.date_added = now

        self.date_modified = now

        super(CreatedMixin, self).save()

    class Meta:
        abstract = True

