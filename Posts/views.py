from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import Post
from .serializer import PostSerializer
from django.http import Http404
from trihub.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()