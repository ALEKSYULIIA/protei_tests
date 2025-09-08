import requests

BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/reverse"

def get_location_info_coord(lat, lon, email = 'mihjn@bk.ru'):
    coord_params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 18,
            "layer": "address"
    }

    headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }
    response = requests.get(BASE_URL_NOMINATIM, params=coord_params, headers=headers)

    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return {}
    data = response.json()
    if data:
            return {
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                 "display_name": data.get("display_name")
            }
    else:
            print("Данные не найдены")
            print(f"Ошибка запроса: {response.status_code}")


result = get_location_info_coord(60.0007332, 30.3092082)
print(result)