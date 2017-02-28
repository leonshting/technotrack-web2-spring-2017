from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from awards.models import AwardType, Award
from likes.models import Like


@receiver(post_save, sender=Like)
def catch_like_awards(instance, *args, **kwargs):
    print("invoked")
    award_types = AwardType.objects.filter(related_content=instance.content_type,
                                           target=ContentType.objects.get_for_model(instance)
                                           )
    model = ContentType.model_class(instance.content_type)
    related_target = model.objects.get(pk=instance.object)
    lc = related_target.likes_count
    print(award_types)
    print(model)
    print(lc)
    print(related_target)
    print(instance.content_type)
    for award_type in award_types:
        if lc == award_type.related_value:
            award = Award.from_target_and_award_type(related_target, award_type)
            award.save()




