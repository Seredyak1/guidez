from rest_framework import permissions

from .models import GuideProfile, GuidePersonalTour


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


class IsTourOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user updating his own profile
    """
    def has_permission(self, request, view):
        #### can write custom code
        if request.method in permissions.SAFE_METHODS:
            return True
        tour = GuidePersonalTour.objects.get(pk=view.kwargs['id'])
        user = tour.profile.auth_user
        if request.user == user:
            return True