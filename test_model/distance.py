import numpy as np
from .models import Paczkomat
import json
from datetime import datetime

#Latitude: 1deg = 110.574km                         #szer
#Longitude: 1 deg = 111.320 * cos(latitude)km       #long


def calc_dist(x1,y1,x2,y2):
    return np.sqrt((x2-x1)^2 + (y2-y1)^2)

def calc_dist_to_km(x1,y1,x2,y2):
    return np.sqrt(np.power(((111.320 * np.cos(y2))*x2-(111.320 * np.cos(y1))*x1), 2) + np.power(((110.574)*y2-(110.574)*y1), 2))

def check_open(data, current_day, time):
    format = '%H:%M'
    opening = datetime.strptime(data["from"], format)
    if(data["to"] == "24:00"):
        closing = datetime.strptime("23:59", format)
    else:
        closing = datetime.strptime(data["to"], format)


    if (datetime.strptime(time, format) - opening).days >= 0 and (closing - datetime.strptime(time, format)).days >= 0:                     #check hour
        if current_day == data["day"] or (data["day"] == "WORKING" and (current_day != "SUNDAY" or current_day != "SATURDAY" ))\
                or (data["day"] == "HOLIDAY" and current_day == "SUNDAY"):    #check day
            return True
    return False

def find_closest(dlug, szer,current_day, time, distance = 3):
    indexes = []
    paczki = Paczkomat.objects.all()
    for paczka in paczki:
        data = paczka.dates
        data = data.replace('},{', '}*{')
        data = data[1:-1].split('*')

        if(len(data) <= 1):
            indexes.append(paczka.id)
        else:
            for day in data:
                day = day.replace('""', '"')
                x = json.loads(day)
                if check_open(x, current_day, time) == True:
                    if calc_dist_to_km(dlug, szer, paczka.dlugosc, paczka.szerokosc) <= distance:
                        indexes.append(paczka.id)

    return indexes