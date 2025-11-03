from rest_framework import serializers
from .models import ArsivEntry, Settings

class ArsivEntrySerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = ArsivEntry
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['join_link']
