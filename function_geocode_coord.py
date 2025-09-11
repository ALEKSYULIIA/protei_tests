import requests

BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/reverse"

def get_location_info_coord(lat, lon, email = 'mihjn@bk.ru'):
    """
    query parameters to get location information at coordinates
                   Parameters:
                               format: response format (json),
                               lat: latitude,
                               lon: longitude,
                               zoom: level of detail required for the address,
                               layer:layer contains all places that make up an address: \
                               address points with house numbers, streets, inhabited places \
                               (suburbs, villages, cities, states etc.) and administrative boundaries
                     Return:
     """
    coord_params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 18,
            "layer": "address"
    }

#  email is needed to avoid 403 response from API server
    headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }

    response = requests.get(BASE_URL_NOMINATIM, params=coord_params, headers=headers)
    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return None

    data = response.json()
    if data:
            return {
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                 "display_name": data.get("display_name")
            }
    else:
            print("Data not found")
            return None

result = get_location_info_coord(60.0007332, 30.3092082)
print(result)