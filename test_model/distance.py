import numpy as np
from .models import Paczkomat

#Latitude: 1deg = 110.574km                         #szer
#Longitude: 1 deg = 111.320 * cos(latitude)km       #long


def calc_dist(x1,y1,x2,y2):
    return np.sqrt((x2-x1)^2 + (y2-y1)^2)

def calc_dist_to_km(x1,y1,x2,y2):
    return np.sqrt(np.power(((111.320 * np.cos(y2))*x2-(111.320 * np.cos(y1))*x1), 2) + np.power(((110.574)*y2-(110.574)*y1), 2))

def find_closest(dlug, szer, distance):
    indexes = []
    paczki = Paczkomat.objects.all()
    for paczka in paczki:
        if calc_dist_to_km(dlug,szer,paczka.dlugosc,paczka.szerokosc) <= distance:
            indexes.append(paczka.id)
    return indexes