import requests

BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/search"

def get_location_info_addr(address, email = 'mihjn@bk.ru'):
    params = {
        "q": address,
        "format": "json",
        "limit": 1,
        }

    headers = {f'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }
    response = requests.get(BASE_URL_NOMINATIM, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return {}

    data = response.json()
    if len(data) == 1:
        first_result = data[0]
        return {
                "address": first_result.get("display_name"),
                "lat": first_result.get("lat"),
                "lon": first_result.get("lon"),
            }
    else:
        print("More than one results")

result = get_location_info_addr("Россия, Санкт-Петербург, Ипподромный переулок, 1 к1")
print(result)
