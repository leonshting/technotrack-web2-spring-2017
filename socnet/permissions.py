from rest_framework import permissions


class IsParticipant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if(obj.author == request.user) or (request.user == obj.recipient):
            return True
        else:
            return False


class IsFoobar(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if(obj.foofriend == request.user) or (request.user == obj.barfriend):
            return True
        else:
            return False


class RestrictNotSafeAllowDelete(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('POST', 'PUT', 'PATCH'):
            return False
        else:
            return True