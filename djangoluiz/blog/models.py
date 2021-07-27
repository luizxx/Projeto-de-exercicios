from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class post(models.model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.foreignkey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DataTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)