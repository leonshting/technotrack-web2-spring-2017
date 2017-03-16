from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from likes.admin import LikeInline
from public.models import Comment, Post


class CommentInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Comment
    can_delete = False
    ct_field = 'content_type'
    ct_fk_field = 'object'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [
            LikeInline,
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        LikeInline,
        CommentInline
    ]
