# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Задаём базовый URL для API Nominatim
BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/reverse"

# Определяем функцию для получения информации о местоположении по координатам
def get_location_info_coord(lat, lon, email = 'mihjn@bk.ru'):
    coord_params = {
            "format": "json",
            "lat": lat,
            "lon": lon,
            "zoom": 18,
            "layer": "address"
    }

#  Задаём заголовок User-Agent с указанием email для идентификации
    headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }

# Отправляем GET-запрос к API
    response = requests.get(BASE_URL_NOMINATIM, params=coord_params, headers=headers)

# Проверяем, что запрос выполнен успешно
    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return {}

# Преобразуем ответ из JSON в Python-объект
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

# Вызываем функцию и выводим результат
result = get_location_info_coord(60.0007332, 30.3092082)
print(result)