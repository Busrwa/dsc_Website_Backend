# blog/serializers.py
from rest_framework import serializers
from .models import Blog
from .utils import upload_file_to_firebase
import os

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.get("image", None)
        instance = Blog.objects.create(**validated_data)

        if image and hasattr(image, "path"):  # görsel varsa
            # Firebase'e yükle
            firebase_url = upload_file_to_firebase(image.path, os.path.basename(image.name))
            # Firebase URL'ini modelde kaydet
            instance.image = firebase_url
            instance.save()

        return instance

    def update(self, instance, validated_data):
        image = validated_data.get("image", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if image and hasattr(image, "path"):  # yeni görsel yüklendiyse
            firebase_url = upload_file_to_firebase(image.path, os.path.basename(image.name))
            instance.image = firebase_url
        instance.save()

        return instance
