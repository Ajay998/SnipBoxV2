from django.contrib import admin
from .models import Tag, Snippet

# Register your models here.
admin.site.register(Tag)
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_by', 'created_at', 'updated_at')  # show in list
    readonly_fields = ("created_at", "updated_at")



