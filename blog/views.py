from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404


class BlogListCreate(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        blogs = Blog.objects.all().order_by('-published_date')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#from django.contrib.auth.models import User

#def create_admin_user():
#    username = "deneme"
#    email = "deneme@gmail.com"
#    password = "deneme"

#    if not User.objects.filter(username=username).exists():
#        User.objects.create_superuser(username=username, email=email, password=password)
#        print("✅ Superuser başarıyla oluşturuldu!")
#    else:
#        print("⚠️ Superuser zaten mevcut.")
