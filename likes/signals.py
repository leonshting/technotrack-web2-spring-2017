from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.db.models import F
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver

from .models import Like


@receiver(pre_save, sender=Like)
def increment_lc(instance, *args, **kwargs):
    model = ContentType.model_class(instance.content_type)
    model.objects.filter(pk=instance.object).update(likes_count=F('likes_count') + 1)


@receiver(pre_delete, sender=Like)
def decrement_lc(instance, *args, **kwargs):
    model = ContentType.model_class(instance.content_type)
    model.objects.filter(pk=instance.object).update(likes_count=F('likes_count') - 1)
