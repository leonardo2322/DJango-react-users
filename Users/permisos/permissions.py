from rest_framework import permissions

class PermissionsOwnProfile(permissions.BasePermission):
    """ esto ayudara con los permisos de actualizacion del user profile"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id