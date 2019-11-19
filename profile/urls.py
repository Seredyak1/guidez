from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('<int:profile_id>/feedback/', GuideProfileFeedbackAPIView.as_view()),
    path('<int:profile_id>/tours/', GuidePersonalTourAPIView.as_view()),
    path('tour/<int:id>/', GuidePersonalTourDetailAPIView.as_view()),
    path('<int:pk>/', GuideProfileAPIView.as_view()),
    path('', GuideProfileListAPIView.as_view()),
]
