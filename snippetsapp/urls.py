from django.urls import path
from .views import SnippetCreateAPIView, SnippetDetailView, SnippetUpdateAPI, SnippetDeleteAPI

app_name = 'snippetsapp'

urlpatterns = [
    path('snippets/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippetUpdateAPI.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippetDeleteAPI.as_view(), name='snippet-delete'),

]