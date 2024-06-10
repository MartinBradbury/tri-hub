from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from.models import Post
from .serializer import PostSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        Likes_count=Count('likes', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile', #show post owner is following
        'likes__owner__profile', #show posts that are liked by a specific user
        'owner__profile' #show posts that are owned by a specific user
    ]

    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'Likes_count',
        'comment_count',
        'likes__created_at',
        'comment__created_at',
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes =[IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comment_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')












# class PostList(generics.ListCreateAPIView):

#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):

#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     queryset = Post.objects.all()