from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from.models import UserPerformance, Event
from .serializer import EventSerializer, PerformanceSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly, SpecificUserFullAccess
from django_filters.rest_framework import DjangoFilterBackend

class EventListView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [SpecificUserFullAccess]
    queryset = Event.objects.all()

class EventListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [SpecificUserFullAccess]
    queryset = Event.objects.all()

class PerformanceListView(generics.ListCreateAPIView):
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserPerformance.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'owner__username',
        'event',
        'time',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PerformanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PerformanceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserPerformance.objects.all()
