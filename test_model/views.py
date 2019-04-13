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
    odlegosc = request.GET.get('odleglosc')
    dzien = request.GET.get("dzien")
    godzina = request.GET.get('godzina')

    if type(odlegosc) is str:
        closest = find_closest((float)(dlugosc),(float)(szerokosc), dzien, godzina, (int)(odlegosc))
    else:
        closest = find_closest((float)(dlugosc), (float)(szerokosc), dzien, godzina)

    return HttpResponse(json.dumps(get_points(closest)), content_type="application/json")

def test_points(request):
    points = []
    points.append(request.GET.get('1'))
    points.append(request.GET.get('2'))
    return HttpResponse(json.dumps(get_points(points)), content_type="application/json")

def map(request):
    dlugosc = request.GET.get('dlugosc')
    szerokosc = request.GET.get('szerokosc') #dont mind me
    odlegosc = request.GET.get('odleglosc')
    dzien = request.GET.get("dzien")
    godzina = request.GET.get('godzina')

    if type(odlegosc) is str:
        closest = find_closest((float)(dlugosc), (float)(szerokosc), dzien, godzina, (int)(odlegosc))
    else:
        closest = find_closest((float)(dlugosc), (float)(szerokosc), dzien, godzina)
    points = get_points(closest)

    context = {'dlugosc': dlugosc,
               'szerokosc': szerokosc,
               'points': points}
    return render(request, 'index.html', context=context)


# Create your views here.

