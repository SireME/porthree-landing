from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PorthreeAboutSerializer, PorthreeFAQSerializer
from .models import PorthreeAbout, PorthreeFAQ

# Create your views here.

class PorthreeAboutView(viewsets.ModelViewSet):
    """setting up PorthreeAbout view

    Args:
        viewsets (_type_): _description_
    """
    serializer_class = PorthreeAboutSerializer
    queryset = PorthreeAbout.objects.all()

class PorthreeFAQView(viewsets.ModelViewSet):
    """setting up PorthreeFAQ view

    Args:
        viewsets (_type_): _description_
    """
    serializer_class = PorthreeFAQSerializer
    queryset = PorthreeFAQ.objects.all()
