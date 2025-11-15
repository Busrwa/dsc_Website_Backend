#events/serializers.py

from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'location', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None