from django.db import models

# Create your models here.

class Paczkomat(models.Model):
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    adress = models.CharField(max_length=128)
    post_code = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    dlugosc = models.FloatField(max_length=128)
    szerokosc = models.FloatField(max_length=128)
    dates = models.CharField(max_length=1024)

