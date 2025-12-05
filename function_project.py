import requests

class Nominatim:
    BASE_URL_SEARCH = "https://nominatim.openstreetmap.org/search"
    BASE_URL_REVERSE = "https://nominatim.openstreetmap.org/reverse"


    def __init__(self, email: str = 'mihjn@bk.ru'):
        self.email = email
        self.headers = {
        'User-Agent': f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      f'Chrome/138.0.0.0 Safari/537.36 ({self.email})'
    }

    def get_location_info_addr(self, address: str):
        params = {
            "q": address,
            "format": "json",
            "limit": 1,
        }

        response = requests.get(self.BASE_URL_SEARCH, params=params, headers=self.headers)
        if response.status_code != 200:
            print(f"Error code: {response.status_code}")
            print(f"Error reason: {response.reason}")
            return {"error": f"HTTP error {response.status_code}: {response.reason}"}
        else:
            data = response.json()
            if len(data) == 1:
                first_result = data[0]
                return {
                    "address": first_result.get("display_name"),
                    "lat": first_result.get("lat"),
                    "lon": first_result.get("lon"),
                }
            elif len(data) > 1:
                print("More than one results")
                first_result = data[0]
                return {
                "address": first_result.get("display_name"),
                "lat": first_result.get("lat"),
                "lon": first_result.get("lon"),
                }
            else:
                return {"error": "No data found for given address"}

    def get_location_info_coord(self, lat, lon):
        params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 18,
            "layer": "address"
        }
        response = requests.get(self.BASE_URL_REVERSE, params=params, headers=self.headers)
        if response.status_code != 200:
            print(f"Error code: {response.status_code}")
            print(f"Error reason: {response.reason}")
            return{"error": f"HTTP error {response.status_code}: {response.reason}"}
        else:
            data = response.json()
            if data:
                return {
                    "lat": data.get("lat"),
                    "lon": data.get("lon"),
                    "display_name": data.get("display_name")
                }
            else:
                print("Data not found")
                return {"error": "No data found for given coordinates"}