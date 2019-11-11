from rest_framework import serializers

from .models import GuideProfile


class GuideProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideProfile
        fields = '__all__'
