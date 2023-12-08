""" views: MainApp views
"""
from django.urls import path
from .views import signup, user_login, user_logout, index
from .views import portfolio
from .views import user_details_form, create_skill, create_project

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('user-details/', user_details_form, name='user-details'),
    path('create-skills/', create_skill, name='create-skills'),
    path('create-project/', create_project, name='create-project'),
    path('edit-project/<uuid:project_id>/', create_project, name='edit-project'),
    path('user/<username>', portfolio, name='portfolio'),
]


# the following settings are to ensuredjango serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
