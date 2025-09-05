import requests
import pytest

address = 'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1'

BASE_URL = "https://nominatim.openstreetmap.org/search"
params = {
    "q": address,
    "format": "json",
    "limit": 1,
}

headers = {'User-Agent':
'Mozilla/5.0 \
(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/138.0.0.0 Safari/537.36 \
(mihjn@bk.ru)'
}

response = requests.get(BASE_URL, params=params, headers=headers)
if response.status_code == 200:
    data = response.json()
    first_result = data[0]
    addr_by_search = first_result.get("display_name")
    lat = first_result.get("lat")
    lon = first_result.get("lon")

    print(f"Адрес: {addr_by_search}")
    print(f"Широта: {lat}")
    print(f"Долгота: {lon}")
else:
    print(f"No results found for '{address}'")


