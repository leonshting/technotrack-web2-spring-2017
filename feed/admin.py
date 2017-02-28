from django.contrib import admin

from feed.models import Event, EventType


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('event_id',)
        return self.readonly_fields
