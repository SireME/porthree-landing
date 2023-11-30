from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator

class PorthreeAbout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    about = models.TextField()
    image = models.ImageField(upload_to='static/images/AboutImage/')


class PorthreeFAQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=200)
    answer = models.TextField()
