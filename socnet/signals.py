from django.db.models import F
from django.db.models.signals import post_save, pre_delete
from django.apps import apps
from django.conf import settings
from django.dispatch import receiver

from .models import Friendship, Friend


@receiver(post_save, sender=Friendship)
def friendship_init_handler(instance, created=False, *args, **kwargs):
    friends = [instance.author, instance.recipient]
    Friend.objects.update_or_create(
        foofriend=friends[1-int(created)],
        barfriend=friends[int(created)],
        defaults={"friendship": instance}
    )


@receiver(pre_delete, sender=Friend)
def friend_delete_handler(instance, *args, **kwargs):
    instance.friendship.author_id = instance.foofriend_id
    instance.friendship.delete()


@receiver(post_save, sender=Friendship)
def increment_fc(instance, created=False, *args, **kwargs):
    if instance.approved:
        a,b = tuple(settings.AUTH_USER_MODEL.split('.'))
        model = apps.get_model(app_label=a, model_name=b)
        model.objects.filter(id=instance.author_id).update(friends_count=F('friends_count') + 1)
        model.objects.filter(id=instance.recipient_id).update(friends_count=F('friends_count') + 1)


@receiver(pre_delete, sender=Friend)
def decrement_fc(instance, *args, **kwargs):
    a,b = tuple(settings.AUTH_USER_MODEL .split('.'))
    model = apps.get_model(app_label=a, model_name=b)
    model.objects.filter(id=instance.foofriend_id).update(friends_count=F('friends_count') - 1)
    model.objects.filter(id=instance.barfriend_id).update(friends_count=F('friends_count') - 1)


