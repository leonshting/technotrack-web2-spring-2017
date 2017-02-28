from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from likes.models import Like


class LikeInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Like
    can_delete = False
    ct_field = 'content_type'
    ct_fk_field = 'object'

