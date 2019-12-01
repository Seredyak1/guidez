from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

from .serializers import *
from .permissions import IsAccountOwner


from django.contrib.auth import get_user_model
User = get_user_model()


class LimitPagination(LimitOffsetPagination):
    default_limit = 20


class UserRegisterAPIView(generics.CreateAPIView):
    """
    Class for user registration.
    create:
    Create new use nad return his own data (without password"
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        out = serializer.data
        out.pop('password', None)
        return Response({'user': out}, status=status.HTTP_201_CREATED)


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class for user profile. Avialable only for login user - else return e,pty user object.
    get:
    Return user profile, depend of request user
    put:
    Update user profile, depend of request user
    patch:
    Partial update user profile, depend of request user
    delete:
    Delete user profile
    """
    permission_classes = (permissions.IsAuthenticated, IsAccountOwner,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        obj = User.objects.get(id=self.request.user.id)
        return obj

    def delete(self, request, *args, **kwargs):
        return Response({'detail': 'Only admin can delete user'}, status=status.HTTP_400_BAD_REQUEST)


class AccountsListAPIView(generics.ListAPIView):
    """
    list:
    Return all users in system exluding invalid
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountsListSerializer
    pagination_class = LimitPagination

    def get_queryset(self):
        return User.objects.all().exclude(is_valid=False)


class AccountDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return user profile by id.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountDetailSerializer

    def get_object(self):
        id = self.kwargs['user_id']
        obj = User.objects.get(id=int(id))
        return obj

