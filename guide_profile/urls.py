from django.urls import path, include

from .views import *


urlpatterns = [
    path('<int:profile_id>/feedback/', GuideProfileFeedbackAPIView.as_view()),
    path('<int:pk>/', GuideProfileAPIView.as_view()),
    path('', GuideProfileListAPIView.as_view()),
]
