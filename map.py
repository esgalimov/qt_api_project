import requests
import sys


def map(coord_1, coord_2, spn, type_of_map, file_name, pt=[]):
    map_request = "https://static-maps.yandex.ru/1.x/"
    params = {
        'll': ','.join([str(coord_1), str(coord_2)]),
        'spn': ','.join([str(spn[0]), str(spn[1])]),
        'l': type_of_map,
        'pt': '~'.join(pt)
    }
    response = requests.get(map_request, params=params)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = file_name
    with open(map_file, "wb") as file:
        file.write(response.content)


# возвращаем координаты объекта
def find_toponym(toponym):
    map_request = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'format': 'json',
        'geocode': toponym,
        'results': '1'
    }

    response = requests.get(map_request, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    else:
        try:
            response_json = response.json()
            toponym = response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            return [float(i) for i in toponym_coodrinates.split()]
        except IndexError:
            pass


if __name__ == '__main__':
    print(find_toponym('Москва'))
