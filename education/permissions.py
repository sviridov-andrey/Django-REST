from rest_framework import permissions
from rest_framework.permissions import BasePermission


class ModerateOrOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator') and permissions.SAFE_METHODS:
            return True

        return request.user == view.get_object().owner
