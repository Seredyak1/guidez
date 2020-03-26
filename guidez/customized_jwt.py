from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import UserProfileSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):
    """
    Customize Data for Login. Return access/refresh data with User data
    """
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        user = User.objects.get(id=self.user.id)
        user_serializer = UserProfileSerializer(instance=user, many=False)
        data['user'] = user_serializer.data
        return data


class TokenObtainPairPatchedView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairPatchedSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
