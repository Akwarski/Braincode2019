from django.shortcuts import render
from django.http import HttpResponse
import json
def home(request):
    return HttpResponse("Hello" + request)

def GPS_GET(request):
    dlugosc = request.GET.get('dlugosc')
    szerokosc = request.GET.get("szerokosc")
    respones_data = {}
    respones_data['dlugosc'] = dlugosc
    respones_data['szerokosc'] = szerokosc
    return HttpResponse(json.dumps(respones_data), content_type="application/json")
    #return HttpResponse("Your gps data is " + dlugosc + " " + szerokosc)
# Create your views here.
