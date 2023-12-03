""" MaxValueValidator: to set integer field max value
    uuid4: to generate a unique user id
"""
from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator



class PostTags(models.Model):
    """
    This model represents the tags for each post
    It has a many to many relationship
    with posts
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    """
    this model holds data associated with a specific
    post
    Note: Many to many relationship exists between
    tag and post
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tags = models.ManyToManyField(PostTags, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(unique=True, null=True, blank=True)
    like = models.BooleanField(default=False, unique=True, null=True, blank=True)
    shared = models.BooleanField(default=False)

    def get_post_tags(self):
        """gets the posts tags

        Returns:
            _tuple_: a tuple containing post tags
        """        
        return "\n".join([i.tags for i in self.tags.name()])

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """
    This model handles comments per post
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.post.user.username} on post '{self.post.title}'"


class Skill(models.Model):
    """
    This models lists all the skills of a specific user
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    """
    This model contains the social media links
    for a particular user
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.FileField(upload_to="static/icons/")
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Hero(models.Model):
    """
    This model defines the data for the hero section
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    intro = models.TextField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"Hero headline: {self.headline} for {self.user}"


class Theme(models.Model):
    """
    This model defines the theme of a specific user
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    primary_color = models.CharField(max_length=255, unique=True, null=True, blank=True)
    secondary_color = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )

    def __str__(self):
        return f"Theme for {self.user}"


class Project(models.Model):
    """
    This model describes the programmers projects
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(5)], null=True, blank=True
    )

    def __str__(self):
        return f"Project by {self.user}"


class ProjectTools(models.Model):
    """
    this model defines the tools used for a
    specific project
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Tool '{self.name}' for project by {self.user}"


class ProjectSkills(models.Model):
    """
    this model defines the skills acquired through a
    specific project
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

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
