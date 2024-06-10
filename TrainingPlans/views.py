from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import TrainingPlan
from .serializer import TrainingPlanSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly, SpecificUserFullAccess

class TrainingPlanListView(generics.ListCreateAPIView):
    serializer_class = TrainingPlanSerializer
    permission_classes = [SpecificUserFullAccess]
    queryset = TrainingPlan.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TrainingPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TrainingPlan.objects.all()