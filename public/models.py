from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from abstracts.models import AuthoredMixin, CreatedMixin, GenericRelatedMixin
from feed.models import EventableMixin
from likes.models import LikableMixin


class Comment(AuthoredMixin, CreatedMixin, LikableMixin, EventableMixin, GenericRelatedMixin):

    content = models.TextField()

    def __str__(self):
        return "Comment by {} to {} {} ".format(self.author,
                                                ContentType.model_class(self.content_type).__name__,
                                                self.object)


class CommentableMixin(models.Model):
    comments = GenericRelation(Comment, content_type_field='content_type', object_id_field='object')
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Post(AuthoredMixin, CreatedMixin, LikableMixin, EventableMixin, CommentableMixin):
    content = models.TextField()

    def __str__(self):
        return "Post {}".format(self.pk)


