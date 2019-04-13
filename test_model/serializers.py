from rest_framework import serializers
from .models import Paczkomat

class PaczkomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paczkomat
        fields = ('type', 'name', 'adress', 'post_code', 'city', 'dlugosc', 'szerokosc', 'dates')

