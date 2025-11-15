#home/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Settings, ArsivEntry
from .serializers import SettingsSerializer, ArsivEntrySerializer
from .permissions import IsAdminOrReadOnly


class SettingsView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        setting = Settings.objects.first()
        serializer = SettingsSerializer(setting)
        return Response(serializer.data)


class ArsivEntryListView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        entries = ArsivEntry.objects.all().order_by("year")
        serializer = ArsivEntrySerializer(entries, many=True)
        return Response(serializer.data)