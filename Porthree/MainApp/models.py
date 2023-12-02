""" MaxValueValidator: to set integer field max value
    uuid4: to generate a unique user id
"""
from uuid import uuid4
from django.db import models
# from django.core.validators import MaxValueValidator


class PorthreeAbout(models.Model):
    """Defines the PorthreeAbout model

    Args:
        models (_object_): django model
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(upload_to="static/images/AboutImage/")

    def __str__(self):
        return str(self.title)


class PorthreeFAQ(models.Model):
    """Defines the PorthreeFAQ model

    Args:
        models (_object_): django model
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return str(self.question)
