from django.contrib.contenttypes.models import ContentType
from feed.models import EventType, Event, EventableMixin
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save)
def create_event_on_eventable_save(instance, created=False, *args, **kwargs):
    if issubclass(instance.__class__, EventableMixin):
        event_type = EventType.objects.get(
            content_type=ContentType.objects.get_for_model(instance),
            created=created
        )
        event = Event.from_instance_and_event_type(instance, event_type)
        event.save()


@receiver(pre_delete)
def create_event_on_eventable_delete(instance, *args, **kwargs):
    if issubclass(instance.__class__, EventableMixin):
        event_type = EventType.objects.get(
            content_type=ContentType.objects.get_for_model(instance),
            created=False,
            modified=False
        )
        event = Event.from_instance_and_event_type(instance, event_type)
        event.save()