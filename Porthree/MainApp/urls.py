""" views: MainApp views
"""
from django.urls import path
from .views import signup, user_login, user_logout, index
from .views import portfolio, blog_post, case_study
from .views import user_details_form, blog_home, projects, resume, contact

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('user/<username>', portfolio, name='portfolio'),
    path('user/<username>/user-details/', user_details_form, name='user-details'),
    # this parts are just for template dummy data display yet to be functional
    path('blogs/', blog_home, name='blogs'),
    path('blog_post/', blog_post, name='blog_post'),
    path('projects/', projects, name='projects'),
    path('case_study/', case_study, name='case_study'),
    path('resume/', resume, name='resume'),
    path('contact/', contact, name='contact'),
]


# the following settings are to ensuredjango serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
