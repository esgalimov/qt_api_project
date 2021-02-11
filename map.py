import requests
import sys


def map(coord_1, coord_2, spn):
    map_request = "http://static-maps.yandex.ru/1.x/"
    params = {
        'll': ','.join([str(coord_1), str(coord_2)]),
        'spn': ','.join([str(spn), str(spn)]),
        'l': 'map'
    }
    response = requests.get(map_request, params=params)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


