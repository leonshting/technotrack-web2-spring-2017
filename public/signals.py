from django.db.models import F
from django.db.models.signals import post_save,pre_delete
from .models import Comment, Post
from django.dispatch import receiver


@receiver(post_save, sender=Comment)
def increment_cc(instance, created=False, *args, **kwargs):
    if created:
        Post.objects.filter(pk=instance.post.pk).update(comments_count=F('comments_count') + 1)


@receiver(pre_delete, sender=Comment)
def decrement_cc(instance, *args, **kwargs):
    Post.objects.filter(pk=instance.post.pk).update(comments_count=F('comments_count') - 1)

