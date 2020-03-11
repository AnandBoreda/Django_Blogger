from django.shortcuts import render
from rest_framework import generics, permissions
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TechCicadaByAnandBoreda(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer