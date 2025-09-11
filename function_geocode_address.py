import requests

BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/search"

def get_location_info_addr(address, email = 'mihjn@bk.ru'):
    """
            query parameters to get location information at address
                Parameters:
                    q: free-form query string to search for address
                    format: response format (json)
                    limit: limit the number of results (default 1)
                Return:
    """
    params = {
        "q": address,
        "format": "json",
        "limit": 1,
    }

# email is needed to avoid 403 response from API server
    headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }

    response = requests.get(BASE_URL_NOMINATIM, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return None

    data = response.json()
# server can respond with not only one address, it’s bad
    if len(data) == 1:
        first_result = data[0]
        return {
                "address": first_result.get("display_name"),
                "lat": first_result.get("lat"),
                "lon": first_result.get("lon"),
            }
    else:
        print("More than one results")
        return None

result = get_location_info_addr("Россия, Санкт-Петербург, Ипподромный переулок, 1 к1")
print(result)
