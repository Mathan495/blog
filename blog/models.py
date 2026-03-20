from django.db import models
from django.utils.text import slugify
import uuid

# category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(uuid.uuid4())[:5]
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.title 

class Aboutus(models.Model):
    content = models.TextField()