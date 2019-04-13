from test_model.models import Paczkomat

def get_points(punkty):
    print(punkty)
    data = []
    data_json = []
    for punkt in punkty:
        obj = Paczkomat.objects.get(id=punkt)
        print(obj)
        data.append(obj)
    for data_point in data:
        one_data = {}
        one_data['type'] = data_point.type
        one_data['name'] = data_point.name
        one_data['adress'] = data_point.adress
        one_data['post_code'] = data_point.post_code
        one_data['city'] = data_point.city
        one_data['dlugosc'] = data_point.dlugosc
        one_data['szerokosc'] = data_point.szerokosc
        #one_data['dates'] = object.dates
        print(one_data)
        data_json.append(one_data)

    return data_json

