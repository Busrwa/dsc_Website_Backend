from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            return obj.image.url   # Cloudinary tam URL
        return None
