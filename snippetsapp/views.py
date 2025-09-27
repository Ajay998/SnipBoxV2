from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet
from .serializers import SnippetSerializer, SnippetDetailSerializer
from rest_framework import generics, permissions

# Create your views here.
class SnippetCreateAPIView(generics.CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SnippetDetailView(generics.RetrieveAPIView):
    serializer_class = SnippetDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Snippet.objects.filter(created_by=user)

class SnippetUpdateAPI(generics.RetrieveUpdateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Snippet.objects.filter(created_by=user)
