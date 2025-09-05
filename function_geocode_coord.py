import requests


def get_location_info_coord(lat, lon):
    base_url_nominatim = "https://nominatim.openstreetmap.org/reverse"
    coord_params = {
    "format": "json",
    "lat": lat,
    "lon": lon,
    "zoom": 18,
    "layer": "address"
    }

    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 (mihjn@bk.ru)'
    }
    response = requests.get(base_url_nominatim, params=coord_params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
             return {
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                 "display_name": data.get("display_name")
            }

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