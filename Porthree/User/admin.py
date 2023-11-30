from django.contrib import admin
from .models import User, PostTags, Post, Comment, Skill, Social, Hero, Theme, Project, ProjectTools

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'email', 'career_title', 'user_name',
    'phone_number', 'first_name', 'last_name', 'rating', 'password', 'resume', )

class PostTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_post', 'user', 'title', 'created_at', 'updated_at', 'content',
    'like', 'shared', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'created_at', 'updated_at', 'content', 'like',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'name',)

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'icon', 'name', 'url',)

class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'headline', 'intro',)

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'primary_color',
    'secondary_color',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'about', 'comment',
    'rating',)

class ProjectToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'name',)


admin.site.register(User, UserAdmin)
admin.site.register(PostTags, PostTagsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTools, ProjectToolsAdmin)
