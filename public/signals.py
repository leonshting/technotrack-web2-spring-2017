from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from django.db.models.signals import post_save,pre_delete
from .models import Comment
from django.dispatch import receiver


@receiver(post_save, sender=Comment)
def increment_cc(instance, created=False, *args, **kwargs):
    if created:
        model = ContentType.model_class(instance.content_type)
        model.objects.filter(pk=instance.object).update(comments_count=F('comments_count') + 1)
        model.objects.filter(pk=instance.object).update(comments_count=F('comments_count') - 1)


@receiver(pre_delete, sender=Comment)
def decrement_cc(instance, *args, **kwargs):
    model = ContentType.model_class(instance.content_type)
    model.objects.filter(pk=instance.object).update(comments_count=F('comments_count') - 1)

