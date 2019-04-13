import numpy as np
from .models import Paczkomat
import json
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

#Latitude: 1deg = 110.574km                         #szer
#Longitude: 1 deg = 111.320 * cos(latitude)km       #dlug


def calc_dist(x1,y1,x2,y2):
    return np.sqrt((x2-x1)^2 + (y2-y1)^2)


def calc_dist_to_km(x1,y1,x2,y2):
    return np.sqrt(np.power(((111.320 * np.cos(y2))*x2-(111.320 * np.cos(y1))*x1), 2) + np.power(((110.574)*y2-(110.574)*y1), 2))


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def check_open(data, current_day, time):
    formatT = '%H:%M'
    opening = datetime.strptime(data["from"], formatT)
    if data["to"] == "24:00":
        closing = datetime.strptime("23:59", formatT)
    else:
        closing = datetime.strptime(data["to"], formatT)

    if (datetime.strptime(time, formatT) - opening).days >= 0 and (closing - datetime.strptime(time, formatT)).days >= 0:                     #check hour
        if current_day == data["day"] or (data["day"] == "WORKING" and (current_day != "SUNDAY" or current_day != "SATURDAY" ))\
                or (data["day"] == "HOLIDAY" and current_day == "SUNDAY"):    #check day
            return True
    return False


def find_closest(dlug, szer, current_day = "", time = "", distance = 3):
    indexes = []
    paczki = Paczkomat.objects.all()

    if(len(time) == 0):
        for paczka in paczki:
            if calc_dist_to_km(dlug, szer, paczka.dlugosc, paczka.szerokosc) <= distance:
                indexes.append((paczka.id, True))
        return indexes
    else:
        for paczka in paczki:

            data = paczka.dates
            data = data.replace('},{', '}*{')
            data = data[1:-1].split('*')

            if len(data) > 1:
                if haversine(dlug, szer, paczka.dlugosc, paczka.szerokosc) <= distance:
                #if calc_dist_to_km(dlug, szer, paczka.dlugosc, paczka.szerokosc) <= distance:
                    for day in data:
                        tempDay = day
                        day = day.replace('""', '"')
                        x = json.loads(day)
                        if check_open(x, current_day, time) is True:
                            indexes.append((paczka.id, True))
                        elif tempDay == data[len(data)-1]:
                            print(paczka.id)
                            indexes.append((paczka.id, False))
        return indexes
