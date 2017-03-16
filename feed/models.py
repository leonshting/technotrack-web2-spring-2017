from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from abstracts.models import CreatedMixin, AuthoredMixin, GenericRelatedMixin
from django.conf import settings


#TODO: deletetion events for every eventable or throw
class EventType(models.Model):

    event_name = models.TextField()
    event_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    created = models.BooleanField(default=False)
    modified = models.BooleanField(default=False)

    def __str__(self):
        return "{} event on {}".format(self.event_name, self.content_type)


class Event(AuthoredMixin, CreatedMixin, GenericRelatedMixin):

    event_type = models.ForeignKey(EventType, null=True, blank=True)
    related_author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='related_author')

    @classmethod
    def from_instance_and_event_type(cls, instance, event_type, author_id=None, author_from_instance=True):

        if hasattr(instance, 'content_object') and issubclass(instance.content_object.__class__, AuthoredMixin):
            related_author = instance.content_object.author
        else:
            related_author = None

        return cls(
            content_type=ContentType.objects.get_for_model(instance),
            object=instance.pk,
            author_id=instance.author_id if author_from_instance else author_id,
            event_type=event_type,
            related_author=related_author
            )

    def __str__(self):
        return "{} event on {} {}".format(
            self.event_type.event_name,
            self.content_type,
            self.object
        )


class EventableMixin(models.Model):
    events = GenericRelation(Event, object_id_field='object', content_type_field='content_type')
    #TODO: what to do with cascade deletion of events?
    class Meta:
        abstract = True

