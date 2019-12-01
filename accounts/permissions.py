from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user updating /deleting his own user profile
    """
    def has_object_permission(self, request, view, obj):
        if request.user is not None:
            if obj == request.user:
                return True
        else:
            return False
