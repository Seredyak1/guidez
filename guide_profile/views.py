from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets

from .models import *
from .serializers import *


class GuideProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GuideProfileSerializer

    def get_object(self):
        return GuideProfile.objects.get(auth_user=self.request.user)

    def get_queryset(self):
        qs = self.get_object()
        return qs
