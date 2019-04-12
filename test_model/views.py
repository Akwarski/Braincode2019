from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello" + request)

def GPS_GET(request):
    dlugosc = request.GET.get('dlugosc')
    szerokosc = request.GET.get("szerokosc")
    return HttpResponse("You just got your gps data " + dlugosc + " " + szerokosc)
# Create your views here.
