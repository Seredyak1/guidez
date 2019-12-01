from rest_framework import serializers

from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    """Return Language detail"""
    class Meta:
        model = Language
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer for creation User. Set required fields and call the method from UserManager
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'validation_image',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data.pop('email'), **validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for User profile. Include information about user languages"""
    languages = serializers.SerializerMethodField()
    language = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Language.objects.all())

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'languages', 'language', 'email', 'city', 'phone',
                  'date_of_birth', 'personal_description', 'profile_image', 'is_valid', )
        read_only_fields = ('is_valid', 'id')

    def get_languages(self, instance):
        serializer = LanguageSerializer(instance=instance.language, many=True)
        return serializer.data


class AccountsListSerializer(serializers.ModelSerializer):
    """Serializer for Users list"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'city')


class AccountDetailSerializer(serializers.ModelSerializer):
    """Serializer for User detail. Include information about user languages"""
    languages = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'languages', 'email', 'city', 'phone', 'date_of_birth',
              'personal_description', 'profile_image',)

    def get_languages(self, instance):
        serializer = LanguageSerializer(instance=instance.language, many=True)
        return serializer.data
