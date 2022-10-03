from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from tinymce import models as tinymce_models


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

    category_tags = Category.objects.all().values_list('name', 'name')

    choice_list = []
    for item in category_tags:
        choice_list.append(item)

    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, unique_for_date='created_on')
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    text = tinymce_models.HTMLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    category = models.CharField(max_length=255, choices=choice_list,default="coding")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("home")
    
    class Meta:
        ordering = ['-created_on']