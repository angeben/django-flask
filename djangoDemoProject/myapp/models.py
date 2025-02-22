from django.db import models

# Create your models here.
class Quote(models.Model):
    content = models.TextField()    
    origin = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    public = models.BooleanField()
    image = models.ImageField(default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()