from django.urls import path

from .views import *

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('profile/', UserProfileAPIView.as_view()),
    path('', AccountsListAPIView.as_view()),
    path('<uuid:user_id>/', AccountDetailAPIView.as_view())
]
