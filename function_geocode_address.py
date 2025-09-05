import requests


def get_location_info_addr(address):
    base_url_nominatim = "https://nominatim.openstreetmap.org/search"
    params = {
    "q": address,
    "format": "json",
    "limit": 1,
    }

    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 (mihjn@bk.ru)'
    }
    response = requests.get(base_url_nominatim, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            first_result = data[0]
            return {
                "address": first_result.get("display_name"),
                "lat": first_result.get("lat"),
                "lon": first_result.get("lon"),
            }
    else:
        print("Пустой список результатов")
        print(f"Ошибка запроса: {response.status_code}")

result = get_location_info_addr("Россия, Санкт-Петербург, Ипподромный переулок, 1 к1")
print(result)