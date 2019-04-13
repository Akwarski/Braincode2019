from django.shortcuts import render
from django.http import HttpResponse
import json
from .get_points import get_points
from .distance import find_closest

def home(request):
    return HttpResponse("Hello" + request)

def GPS_GET(request):
    dlugosc = request.GET.get('dlugosc')
    szerokosc = request.GET.get("szerokosc")
    

    respones_data = {}

    respones_data['dlugosc'] = dlugosc
    respones_data['szerokosc'] = szerokosc

    closest = find_closest((float)(dlugosc),(float)(szerokosc), 100)

    return HttpResponse(json.dumps(get_points(closest)), content_type="application/json")

def test_points(request):
    points = []
    points.append(request.GET.get('1'))
    points.append(request.GET.get('2'))
    return HttpResponse(json.dumps(get_points(points)), content_type="application/json")


# Create your views here.
