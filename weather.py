import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 55.7522,
    "longitude": 37.6156,
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
    "timezone": "Europe/Moscow"
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    today_temp_min = data['daily']['temperature_2m_min'][0]
    today_temp_max = data['daily']['temperature_2m_max'][0]
    today_precipitation = data['daily']['precipitation_sum'][0]

    print(f"Прогноз погоды в Москве на сегодня:")
    print(f"Минимальная температура: {today_temp_min}°C")
    print(f"Максимальная температура: {today_temp_max}°C")
    print(f"Ожидаемое количество осадков: {today_precipitation} мм")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

