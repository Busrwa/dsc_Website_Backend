#home/serializers.py

from rest_framework import serializers
from .models import ArsivEntry, Settings


class ArsivEntrySerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = ArsivEntry
        fields = ['id', 'name', 'year', 'photo', 'description', 'created_at']

    def get_photo(self, obj):
        if obj.photo:
            return obj.photo.url
        return None


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['join_link']