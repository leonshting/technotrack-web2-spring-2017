from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from abstracts.models import AuthoredMixin, CreatedMixin
from feed.models import EventableMixin
from likes.models import LikableMixin


#TODO: probably should make comment generic related, i.e. we need to comment some other things but posts
class Comment(AuthoredMixin, CreatedMixin, LikableMixin, EventableMixin):
    content = models.TextField()
    post = models.ForeignKey('public.Post')

    def __str__(self):
        return "Comment by {} to post {} ".format(self.author, self.post_id)


class CommentableMixin(models.Model):
    comments = GenericRelation(Comment, content_type_field='content_type', object_id_field='object')
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Post(AuthoredMixin, CreatedMixin, LikableMixin, EventableMixin, CommentableMixin):
    content = models.TextField()

    def __str__(self):
        return "Post {}".format(self.pk)


