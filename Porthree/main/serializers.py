from rest_framework import serializers
from .models import PorthreeAbout, PorthreeFAQ
from .models import User, Skill, Social, Hero
from .models import PostTags, Post, Comment
from .models import Theme, Project, ProjectTools

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTags
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTools
        fields = '__all__'

class PorthreeAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PorthreeAbout
        fields = ('id', 'created_at',
                    'updated_at', 'about',
                    'image')

class PorthreeFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PorthreeFAQ
        fields = ('id', 'created_at',
                    'updated_at', 'question',
                    'answer')
