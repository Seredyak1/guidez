from django.urls import path, include

from .views import *


urlpatterns = [
    path('', GuideProfileAPIView.as_view()),
]
