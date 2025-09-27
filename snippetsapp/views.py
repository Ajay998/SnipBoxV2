from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet, Tag
from .serializers import SnippetSerializer, SnippetDetailSerializer, SnippetDeleteSerializer, TagSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

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

class SnippetDeleteAPI(generics.RetrieveDestroyAPIView):
    serializer_class = SnippetDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        snippet_instance = self.get_object()
        self.perform_destroy(snippet_instance)
        remaining_available_snippets = Snippet.objects.filter(created_by=request.user)
        if remaining_available_snippets.exists():
            serializer = SnippetSerializer(remaining_available_snippets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No snippets remaining."}, status=status.HTTP_204_NO_CONTENT)

class OverviewAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        total_snippets = Snippet.objects.filter(created_by=request.user)
        return Response({
            "total_snippets": total_snippets.count(),
            "snippets_details": {"snippets": [{"id": s.id, "title": s.title, "detail_url": f"/api/snippets/{s.id}/"} for s in total_snippets]}
        })

class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tag.objects.all()



    
