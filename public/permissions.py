from rest_framework import permissions

from abstracts.models import AuthoredMixin


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff


SECONDS_FOR_EDITION = 60
class TimeFromCreation(permissions.BasePermission):

    message = 'Editing the comment is allowed only 60 seconds after its creation.'

    def has_object_permission(self, request, view, obj):
        from django.utils import timezone
        if (request.method == 'PUT' or request.method == 'PATCH') \
                and (timezone.now() - obj.date_added).total_seconds() < SECONDS_FOR_EDITION:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False



#TODO: another ways of restricting size of responses?
class SpecifyFilters(permissions.BasePermission):

    message = 'You must specify filtering criterion'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif len(request.query_params) == 0:
            return False


class IsFriend(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_friend(obj.author) or request.user == obj.author


class IsCommentRelatedToFriendObject(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return issubclass(AuthoredMixin, obj.content_object.__class__) and \
            request.user.is_friend(obj.content_object.author)
