#team/serializers.py

from rest_framework import serializers
from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'photo', 'bio']

    def get_photo(self, obj):
        if obj.photo:
            return obj.photo.url
        return None