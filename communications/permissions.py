from rest_framework import permissions


class IsChatParticipant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request.user in obj.chat.users.all())
        return request.user in obj.chat.users.all()

