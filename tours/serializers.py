from rest_framework import serializers

from .models import GuidePersonalTour


class GuidePersonalTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuidePersonalTour
        fields = '__all__'
