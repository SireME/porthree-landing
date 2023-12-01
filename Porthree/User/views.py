""" importing modules from models for accessing database data
    importing modules from serializers for rest api data
"""
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, PostTagsSerializer, PostSerializer, CommentSerializer, SkillSerializer, SocialSerializer, HeroSerializer, ThemeSerializer, ProjectSerializer, ProjectToolsSerializer
from .models import User, PostTags, Post, Comment, Skill, Social, Hero, Theme, Project, ProjectTools
# Create your views here.


class UserView(viewsets.ModelViewSet):
    """ setting up User django view class to
    extract all table data
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostTagsView(viewsets.ModelViewSet):
    """ setting up PostTags django view class to
    extract all table data
    """
    serializer_class = PostTagsSerializer
    queryset = PostTags.objects.all()


class PostView(viewsets.ModelViewSet):
    """ setting up Post django view class to
    extract all table data
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(viewsets.ModelViewSet):
    """ setting up Comment django view class to
    extract all table data
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class SkillView(viewsets.ModelViewSet):
    """ setting up Skill django view class to
    extract all table data
    """
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

class SocialView(viewsets.ModelViewSet):
    """ setting up Social django view class to
    extract all table data
    """
    serializer_class = SocialSerializer
    queryset = Social.objects.all()

class HeroView(viewsets.ModelViewSet):
    """ setting up Hero django view class to
    extract all table data
    """
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()

class ThemeView(viewsets.ModelViewSet):
    """ setting up Theme django view class to
    extract all table data
    """
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()

class ProjectView(viewsets.ModelViewSet):
    """ setting up Project django view class to
    extract all table data
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectToolsView(viewsets.ModelViewSet):
    """ setting up ProjectTools django view class to
    extract all table data
    """
    serializer_class = ProjectToolsSerializer
    queryset = ProjectTools.objects.all()

