import requests
import sys


def map(coord_1, coord_2, spn, type_of_map, file_name):
    map_request = "http://static-maps.yandex.ru/1.x/"
    params = {
        'll': ','.join([str(coord_1), str(coord_2)]),
        'spn': ','.join([str(spn), str(spn)]),
        'l': type_of_map
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


