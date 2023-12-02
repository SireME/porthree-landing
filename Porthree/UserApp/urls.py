""" views: MainApp views
"""
from django.urls import path
from . import views

urlpatterns = [
    # come back for this (should be a dynamic url path)
    path("", views.portfolio, name="portfolio"),
]
