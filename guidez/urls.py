"""guidez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenRefreshView
from .customized_jwt import TokenObtainPairPatchedView

swagger = get_swagger_view(title='Guidez API')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/',  TokenObtainPairPatchedView.as_view()),
    path('accounts/refresh-token/', TokenRefreshView.as_view()),
    path('accounts/', include('accounts.urls')),

    path('blogs/', include('blog.urls')),
    path('order/', include('order.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path('', swagger),
    ]
