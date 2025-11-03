from rest_framework import serializers
from .models import Event
from .utils import upload_file_to_firebase

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        file = self.context['request'].FILES.get('image')
        if file:
            validated_data['image'] = upload_file_to_firebase(file)
        return super().create(validated_data)
