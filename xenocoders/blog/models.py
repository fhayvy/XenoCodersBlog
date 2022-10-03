from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("home")

class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="blog_category")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("home")
    
    class Meta:
        ordering = ['-created_on']