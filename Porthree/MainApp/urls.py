""" views: MainApp views
"""
from django.urls import path
from .views import signup, user_login, user_logout, index
from .views import portfolio

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('<username>', portfolio, name='portfolio'),
]
