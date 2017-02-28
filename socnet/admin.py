from django.contrib import admin
from .models import *


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendsAdmin(admin.ModelAdmin):
    pass

