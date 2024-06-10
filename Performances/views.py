from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import UserPerformance, Event
from .serializer import EventSerializer, PerformanceSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly




class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventListDetailView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class PerformanceListView(generics.ListCreateAPIView):
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserPerformance.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PerformanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PerformanceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserPerformance.objects.all()
