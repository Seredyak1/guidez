from django_filters import rest_framework as filters

from .models import GuidePersonalTour

from django.contrib.auth import get_user_model
User = get_user_model()


class GuidePersonalTourFilter(filters.FilterSet):
    user = filters.CharFilter(field_name="user_id")

    class Meta:
        model = GuidePersonalTour
        fields = ('user',)
