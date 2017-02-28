from django.contrib import admin

from awards.models import AwardType, Award


@admin.register(AwardType)
class AwardTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass