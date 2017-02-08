from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendsAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
