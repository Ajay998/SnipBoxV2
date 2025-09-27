from django.urls import path
from .views import SnippetCreateAPIView, SnippetDetailView, SnippetUpdateAPI, SnippetDeleteAPI, OverviewAPI, TagDetailView, TagListView

app_name = 'snippetsapp'

urlpatterns = [
    path('snippets/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippetUpdateAPI.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippetDeleteAPI.as_view(), name='snippet-delete'),
    path('snippets/overview/', OverviewAPI.as_view(), name='snippet-overview'),
    path('tags/', TagListView.as_view(), name='list-tags'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail')

]