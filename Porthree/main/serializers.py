from rest_framework import serializers
from .models import PorthreeAbout, PorthreeFAQ


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
