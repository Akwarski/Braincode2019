from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello" + request)

def GPS_GET(request):
    return HttpResponse("You just got your gps data")
# Create your views here.
