from django.db import models
from django.conf import settings
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.title = self.title.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Snippet(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='snippets', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']