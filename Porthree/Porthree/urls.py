"""
URL configuration for Porthree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main import views
from User import views as userViews

router = routers.DefaultRouter()
router.register(r'PothreeAbout', views.PorthreeAboutView, 'about')
router.register(r'PothreeFAQ', views.PorthreeFAQView, 'FAQ')

router.register(r'User', userViews.UserView, 'User')
router.register(r'PostTags', userViews.PostTagsView, 'PostTags')
router.register(r'Post', userViews.PostView, 'Post')
router.register(r'Comment', userViews.CommentView, 'Comment')
router.register(r'Skill', userViews.SkillView, 'Skill')
router.register(r'Social', userViews.SocialView, 'Social')
router.register(r'Hero', userViews.HeroView, 'Hero')
router.register(r'Theme', userViews.ThemeView, 'Theme')
router.register(r'Project', userViews.ProjectView, 'Project')
router.register(r'ProjectTools', userViews.ProjectToolsView, 'ProjectTools')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
