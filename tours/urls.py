from django.urls import path, include
from rest_framework import routers

from .views import *


router_tour = routers.DefaultRouter()
router_tour.register('', GuidePersonalTourAPIView, basename='personal_tour')

urlpatterns = [
    path("", include(router_tour.urls)),
]
