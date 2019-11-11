from rest_framework import permissions

from .models import GuideProfile

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # need obj.user for post model
        # obj here is a UserProfile instance
        profile = GuideProfile.objects.get(auth_user=request.user)
        return obj == profile
