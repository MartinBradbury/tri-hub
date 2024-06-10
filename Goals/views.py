from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import Goal
from .serializer import GoalSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly, IsAuthOrReadOnly

class GoalList(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthOrReadOnly]
    queryset = Goal.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GoalDetailList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Goal.objects.all()