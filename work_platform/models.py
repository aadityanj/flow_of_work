from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
class JobTitles(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    skills = models.ManyToManyField(Skills)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']









