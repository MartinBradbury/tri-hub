from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from .models import Profile
from .serializer import ProfileSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        post_count = Count('owner__post', distinct=True),
        follower_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),

    ).order_by('-created_at')


    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'owner__username',
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile', # get all profiles that are followed by a profile, given its id
    ]
    
    ordering_fields = [
        'post_count',
        'follower_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

        

class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes =[IsOwnerOrReadOnly]
    queryset = Profile.objects.all()