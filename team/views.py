#team/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TeamMember
from .serializers import TeamMemberSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly

class TeamListCreate(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        members = TeamMember.objects.all()
        serializer = TeamMemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        member = get_object_or_404(TeamMember, pk=pk)
        serializer = TeamMemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        member = get_object_or_404(TeamMember, pk=pk)
        serializer = TeamMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = get_object_or_404(TeamMember, pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
