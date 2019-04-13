from test_model.models import Paczkomat


def get_points(punkty):
    data = []
    data_json = []
    for punkt, if_open in punkty:
        obj = Paczkomat.objects.get(id=punkt)
        data.append((obj, if_open))

    for object in data:
        one_data = {}
        one_data['type'] = object[0].type
        one_data['name'] = object[0].name
        one_data['adress'] = object[0].adress
        one_data['post_code'] = object[0].post_code
        one_data['city'] = object[0].city
        one_data['dlugosc'] = object[0].dlugosc
        one_data['szerokosc'] = object[0].szerokosc
        one_data['otwarte'] = object[1]
        #one_data['dates'] = object.dates
        data_json.append(one_data)

    return data_json

