from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics, permissions

# Create your views here.
class SnippetCreateAPIView(generics.CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

