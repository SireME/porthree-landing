from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PorthreeAboutSerializer, PorthreeFAQSerializer
from .models import PorthreeAbout, PorthreeFAQ

# user and serializer
from .models import User
from .serializers import UserSerializer

# posttags and serializer
from .models import PostTags
from .serializers import PostTagsSerializer

# post and serializer
from .models import Post
from .serializers import PostSerializer

# comments and serialiser
from .models import Comment
from .serializers import CommentSerializer

# skill and serializer
from .models import Skill
from .serializers import SkillSerializer

# social and serializer
from .models import Social
from .serializers import SocialSerializer

# hero and serializer
from .models import Hero
from .serializers import HeroSerializer

# theme and serializer
from .models import Theme
from .serializers import ThemeSerializer

# project and serializer
from .models import Project
from .serializers import ProjectSerializer

# projecttools and serializer
from .models import ProjectTools
from .serializers import ProjectToolsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostTagsViewSet(viewsets.ModelViewSet):
    queryset = PostTags.objects.all()
    serializer_class = PostTagsSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectToolsViewSet(viewsets.ModelViewSet):
    queryset = ProjectTools.objects.all()
    serializer_class = ProjectToolsSerializer

class PorthreeAboutView(viewsets.ModelViewSet):
    serializer_class = PorthreeAboutSerializer
    queryset = PorthreeAbout.objects.all()

class PorthreeFAQView(viewsets.ModelViewSet):
    serializer_class = PorthreeFAQSerializer
    queryset = PorthreeFAQ.objects.all()
