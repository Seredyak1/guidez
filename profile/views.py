from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import *
from .serializers import *
from .permissions import IsOwner, IsTourOwner


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


class GuidePersonalTourAPIView(generics.ListCreateAPIView):
    """
    Added personal for GuideProfile.
    :param profile_id in url
    """
    permission_classes = (permissions.AllowAny, permissions.IsAuthenticated)
    serializer_class = GuidePersonalTourSerializer
    lookup_field = 'profile_id'

    def get_queryset(self):
        qs = GuidePersonalTour.objects.filter(profile_id=self.kwargs['profile_id'])
        return qs

    def create(self, request, *args, **kwargs):
        id = self.kwargs['profile_id']
        profile = GuideProfile.objects.get(id=id)
        if profile.auth_user == self.request.user:
            searialazer = self.serializer_class(data=self.request.data)
            searialazer.is_valid(raise_exception=True)
            self.perform_create(searialazer)
            return Response(searialazer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Can create only for self account"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        profile = GuideProfile.objects.get(id=self.kwargs['profile_id'])
        if profile.auth_user == self.request.user:
            serializer.save(profile=profile)


class GuidePersonalTourDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """"""
    permission_classes = (IsTourOwner,)
    serializer_class = GuidePersonalTourSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs['id']
        obj = GuidePersonalTour.objects.get(id=id)
        return obj

    def get_queryset(self):
        qs = self.get_object()
        return qs
