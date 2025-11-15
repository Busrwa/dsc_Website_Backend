#sponsors/serializers.py

from rest_framework import serializers
from .models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'logo', 'website']

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url
        return None