from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from abstracts.models import CreatedMixin, AuthoredMixin
from feed.models import EventableMixin


class AwardType(models.Model):
    award_id = models.AutoField(primary_key=True)
    award_name = models.TextField()
    related_content = models.ForeignKey(ContentType, related_name='related_content', verbose_name='Award on')
    related_value = models.PositiveIntegerField(default=0)
    target = models.ForeignKey(ContentType,
                               related_name='target',
                               verbose_name='Award captured on',
                               null=True,
                               blank=True
                               )

    def __str__(self):
        return "{} on {} greater than {}".format(self.award_name, self.related_content, self.related_value)


#TODO: maybe make it commentable if comment become generic related
class Award(CreatedMixin, AuthoredMixin, EventableMixin):
    award_type = models.ForeignKey(AwardType)
    object = models.PositiveIntegerField()

    @classmethod
    def from_target_and_award_type(cls, target, award_type):
        return cls(
            object=target.pk,
            author_id=target.author_id,
            award_type=award_type
        )

    def __str__(self):
        return "{} award on {} {}".format(self.award_type, self.award_type.related_content, self.object)

class AwardableMixin(models.Model):
    awards = GenericRelation(Award, object_id_field='object', content_type_field='award_type')

    class Meta:
        abstract = True