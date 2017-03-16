from rest_framework import permissions
from abstracts.models import AuthoredMixin


class OwnerOrFriend(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if issubclass(obj.__class__, AuthoredMixin) and \
                (request.user.is_friend(obj.author) or request.user == obj.author):
            return True
        else:
            return False


class IsSafeMethod(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False