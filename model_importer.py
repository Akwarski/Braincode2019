
from test_model.models import Paczkomat

file  = open('/home/filip/Downloads/pickup_points_small_unique.csv', 'r')
next(file)

for line in file:
    line = line.split(';')
    tab = []
    for arg in line:
        arg = arg[1:-1]
        tab.append(arg)
    entry = Paczkomat(type = tab[0], name = tab[1], adress = tab[2], post_code = tab[3], city = tab[4], dlugosc = (float)(tab[5]), szerokosc = (float)(tab[6]), dates = tab[7])
    entry.save()
