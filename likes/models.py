from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from abstracts.models import CreatedMixin, AuthoredMixin
from feed.models import EventableMixin


class Like(AuthoredMixin, CreatedMixin, EventableMixin):
    content_type = models.ForeignKey(ContentType, related_name='content_type')
    object = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object')

    def __str__(self):
        return "like from {} to {} {}".format(self.author, self.content_type, self.object)


class LikableMixin(models.Model):
    likes_count = models.IntegerField(default=0)
    likes = GenericRelation(Like, content_type_field='content_type', object_id_field='object')

    class Meta:
        abstract = True
