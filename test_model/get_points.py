from test_model.models import Paczkomat

def get_points(punkty):
    iterator = 1
    data = []
    data_json = {}
    one_data = {}
    for punkt in punkty:
        obj = Paczkomat.objects.get(id= punkt)
        data.append(obj)
    for object in data:
        one_data['type'] = object.type
        one_data['name'] = object.name
        one_data['adress'] = object.adress
        one_data['post_code'] = object.post_code
        one_data['city'] = object.city
        one_data['dlugosc'] = object.dlugosc
        one_data['szerokosc'] = object.szerokosc
        one_data['dates'] = object.dates
        data_json[str(iterator)] = one_data
        iterator= iterator + 1
    return data_json

