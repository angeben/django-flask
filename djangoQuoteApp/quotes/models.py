from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Quote(models.Model):
    content = models.TextField()    
    origin = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    public = models.BooleanField()
    image = models.ImageField(default='null', upload_to='quotes')
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
        ordering = ['id']
    
    def __str__(self):
        return f"{self.content} - {self.author} - {self.user}"