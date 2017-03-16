from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from abstracts.models import CreatedMixin, AuthoredMixin, GenericRelatedMixin
from feed.models import EventableMixin


class Like(AuthoredMixin, CreatedMixin, EventableMixin, GenericRelatedMixin):

    def __str__(self):
        return "like from {} to {} {}".format(self.author, self.content_type, self.object)


class LikableMixin(models.Model):
    likes_count = models.IntegerField(default=0)
    likes = GenericRelation(Like, content_type_field='content_type', object_id_field='object')

    class Meta:
        abstract = True
