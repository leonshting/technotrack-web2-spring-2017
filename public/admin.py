from django.contrib import admin

from likes.admin import LikeInline
from public.models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False


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
