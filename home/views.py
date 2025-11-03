from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Settings, ArsivEntry
from .serializers import SettingsSerializer, ArsivEntrySerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Settings, ArsivEntry
from .serializers import SettingsSerializer, ArsivEntrySerializer
from .permissions import IsAdminOrReadOnly

# Site ayarları
class SettingsView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        setting = Settings.objects.first()  # tek ayar objesi
        serializer = SettingsSerializer(setting)
        return Response(serializer.data)


# Arşiv girişleri
class ArsivEntryListView(APIView):
    def get(self, request):
        entries = ArsivEntry.objects.all().order_by("year")
        serializer = ArsivEntrySerializer(entries, many=True, context={"request": request})
        return Response(serializer.data)