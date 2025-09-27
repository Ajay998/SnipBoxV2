from django.urls import path
from .views import SnippetCreateAPIView

app_name = 'snippetsapp'

urlpatterns = [
    path('snippets/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
]