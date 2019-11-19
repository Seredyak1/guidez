from rest_framework import serializers

from .models import *


class LanguageAPIVIew(serializers.ModelSerializer):
    """Return Language detail"""
    class Meta:
        model = Language
        fields = '__all__'


class GuideProfileSerializer(serializers.ModelSerializer):
    """Serializer for GuideProfile, use for current register User"""
    class Meta:
        model = GuideProfile
        exclude = ('validation_image', 'is_valid', 'auth_user')


class GuideProfileListSerializer(serializers.ModelSerializer):
    """Serializer for GuideProfile, use for profiles list"""
    class Meta:
        model = GuideProfile
        fields = ('id', 'first_name', 'last_name', 'profile_image', 'language')


class GuideProfileFeedbackSerializer(serializers.ModelSerializer):
    """Serializer for GuideProfileFeedback"""
    class Meta:
        model = GuideProfileFeedback
        fields = '__all__'
        read_only_fields = ('profile', 'published',)


class GuidePersonalTourSerializer(serializers.ModelSerializer):
    """Serializer for GuidePersonalTourSerializer"""
    class Meta:
        model = GuidePersonalTour
        fields = '__all__'
        read_only_fields = ('profile',)