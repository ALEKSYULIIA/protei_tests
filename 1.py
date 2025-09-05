import requests

HEADERS = {
    "User-Agent": "TestNominatimAPI/1.0 (your_email@example.com)"
}

def forward_geocode(address):
    params = {
        "q": address,
        "format": "json",
        "limit": 1,
        "addressdetails": 1
    }
    response = requests.get("https://nominatim.openstreetmap.org/search", params=params, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    if not data:
        print("Forward geocode: no results")
        return None
    place = data[0]
    lat = float(place["lat"])
    lon = float(place["lon"])
    name = place["display_name"]
    print(f"Forward geocode '{address}': lat={lat}, lon={lon}, name={name}")

    # Простая проверка координат (пример для Москвы)
    if 55.5 < lat < 56 and 37 < lon < 38:
        print("Forward geocode: coordinates look correct")
    else:
        print("Forward geocode: coordinates out of expected range")

    return lat, lon, name

def reverse_geocode(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "addressdetails": 1
    }
    response = requests.get("https://nominatim.openstreetmap.org/reverse", params=params, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    name = data.get("display_name", "")
    address = data.get("address", {})
    print(f"Reverse geocode ({lat}, {lon}): name={name}")

    # Проверяем, что в адресе есть Москва
    city = address.get("city") or address.get("town") or address.get("village") or ""
    if "Moscow" in city:
        print("Reverse geocode: address contains Moscow")
    else:
        print("Reverse geocode: address does not contain Moscow")

    return name, address

if __name__ == "__main__":
    # Прямое геокодирование
    forward_geocode("Red Square, Moscow, Russia")

    # Обратное геокодирование
    reverse_geocode(55.7539, 37.6208)


