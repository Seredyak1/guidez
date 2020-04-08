from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import GuidePersonalTour
from .serializers import GuidePersonalTourSerializer
from .permissions import IsTourOwner
from .filters import GuidePersonalTourFilter


from django.contrib.auth import get_user_model
User = get_user_model()


class GuidePersonalTourAPIView(viewsets.ModelViewSet):
    """
    post: Create new Guide Personal Tour, user depend on of request user
    list: Return all Guide Personal Tours. Use filters for slise tours by user id
    get: Return one Guide Personal Tours
    put: Update one Guide Personal Tours. Based on permissions, update tour can only his user owner
    """
    permission_classes = (IsTourOwner,)
    serializer_class = GuidePersonalTourSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_class = GuidePersonalTourFilter
    ordering_fields = ('created_at',)

    def get_queryset(self):
        return GuidePersonalTour.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
