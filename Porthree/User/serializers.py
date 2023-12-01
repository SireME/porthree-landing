from rest_framework import serializers
from .models import User, PostTags, Post, Comment, Skill, Social, Hero, Theme, Project, ProjectTools





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created_at', 'updated_at', 'email',
    'career_title', 'user_name','phone_number', 'first_name',
    'last_name', 'rating', 'password', 'resume', ]


class PostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTags
        fields = ['id', 'created_at', 'updated_at', 'name',]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'get_post', 'user', 'title', 'created_at',
    'updated_at', 'content','like', 'shared', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'created_at', 'updated_at',
    'content', 'like',]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'user', 'created_at', 'updated_at', 'name',]


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'user', 'created_at', 'updated_at', 'icon',
    'name', 'url',]


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'user', 'headline', 'intro',]


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'user', 'created_at', 'updated_at',
    'primary_color','secondary_color',]



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'user', 'created_at', 'updated_at', 'about',
    'comment','rating',]


class ProjectToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTools
        fields = ['id', 'user', 'created_at', 'updated_at', 'name',]
