from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'created_by', 'tags']
        read_only_fields = ['created_at', 'updated_at', 'created_by']

    def create(self, data):
        tags_data = data.pop('tags', [])
        snippet = Snippet.objects.create(**data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            snippet.tags.add(tag)
        return snippet
