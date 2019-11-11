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
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuideProfileListSerializer
    queryset = GuideProfile.objects.filter(is_valid=True)
    pagination_class = LimitPagination


class GuideProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """"""
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = GuideProfileSerializer

    def get_queryset(self):
        return GuideProfile.objects.all()
