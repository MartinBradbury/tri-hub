from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from .models import TrainingPlan
from .serializer import TrainingPlanSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly, SpecificUserFullAccess
from django_filters.rest_framework import DjangoFilterBackend


class TrainingPlanListView(generics.ListCreateAPIView):
    serializer_class = TrainingPlanSerializer
    permission_classes = [SpecificUserFullAccess]
    queryset = TrainingPlan.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'plan_level',
        'weeks_available',
        'hours_available',
        'title',
    ]
    ordering_fields = [
        'plan_level',
        'weeks_available',
        'hours_available',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrainingPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TrainingPlan.objects.all()
