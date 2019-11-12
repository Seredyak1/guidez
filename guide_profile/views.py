from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import *
from .serializers import *
from .permissions import IsOwner


class LimitPagination(LimitOffsetPagination):
    default_limit = 20


class GuideProfileListAPIView(generics.ListAPIView):
    """
    get:
    Return all valid GuideProfile
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuideProfileListSerializer
    queryset = GuideProfile.objects.filter(is_valid=True)
    pagination_class = LimitPagination


class GuideProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for GuideProfile Detail

    get:
    Return GuideProfile by id
    put/patch:
    Change GuideProfile, aviable for GuideProfile owner
    delete:
    Remove GuideProfile, aviable for GuideProfile owner
    """
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = GuideProfileSerializer

    def get_queryset(self):
        return GuideProfile.objects.all()


class GuideProfileFeedbackAPIView(generics.ListCreateAPIView):
    """
    Added feedback for GuideProfile.
    :param profile_id in url
    get:
    Return all feedback for this GuideProfile
    create:
    Create new feedback for GuideProfile, set current profile as profile
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuideProfileFeedbackSerializer
    lookup_field = 'profile_id'

    def get_queryset(self):
        qs = GuideProfileFeedback.objects.filter(profile_id=self.kwargs['profile_id'])
        return qs

    def perform_create(self, serializer):
        profile = GuideProfile.objects.get(id=self.kwargs['profile_id'])
        serializer.save(profile=profile)
