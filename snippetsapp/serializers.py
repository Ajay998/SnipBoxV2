from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_titles = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'created_by', 'tags', 'tag_titles']
        read_only_fields = ['created_at', 'updated_at', 'created_by']

    def create(self, data):
        tag_titles = data.pop('tag_titles', [])
        snippet = Snippet.objects.create(**data)
        for title in tag_titles:
            normalized_title = title.strip().lower()
            tag_obj, _ = Tag.objects.get_or_create(title=normalized_title)
            snippet.tags.add(tag_obj)
        return snippet
    
    def update(self, snippet_instance, data):
        tag_titles = data.pop('tag_titles', [])
        snippet_instance.title = data.get('title', snippet_instance.title)
        snippet_instance.note = data.get('note', snippet_instance.note)
        snippet_instance.save()
        if tag_titles:
            snippet_instance.tags.clear()
            for title in tag_titles:
                normalized_title = title.strip().lower()
                tag_obj, _ = Tag.objects.get_or_create(title=normalized_title)
                snippet_instance.tags.add(tag_obj)
        return snippet_instance

class SnippetDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'created_by', 'tags']
        read_only_fields = ['created_at', 'updated_at', 'created_by']

class SnippetDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id']
