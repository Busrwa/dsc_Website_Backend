#sponsors/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sponsor
from .serializers import SponsorSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly


class SponsorListCreate(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        sponsor = get_object_or_404(Sponsor, pk=pk)
        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data)

    def put(self, request, pk):
        sponsor = get_object_or_404(Sponsor, pk=pk)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sponsor = get_object_or_404(Sponsor, pk=pk)
        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)