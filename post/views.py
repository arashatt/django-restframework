from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #queryset = Post.objects.all()
    
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.request.user
        print(f"***********{user.__dict__}********************")
        return user.post_set.all()
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer
# Create your views here.
