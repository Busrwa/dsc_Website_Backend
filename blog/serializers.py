from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "published_date", "image"]

    def get_image(self, obj):
        if obj.image:
            # Cloudinary URL'i döndür
            return obj.image.url
        return None

    def create(self, validated_data):
        # Görsel upload işlemi otomatik yapılacak
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)