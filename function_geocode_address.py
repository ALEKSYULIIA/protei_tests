# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Задаём базовый URL для API Nominatim
BASE_URL_NOMINATIM = "https://nominatim.openstreetmap.org/search"

# Определяем функцию для получения информации о местоположении по адресу
def get_location_info_addr(address, email = 'mihjn@bk.ru'):
    #  Создаем словарь с параметрами запроса
    params = {
        "q": address,
        "format": "json",
        "limit": 1,
    }

#  Задаём заголовок User-Agent с указанием email для идентификации
    headers = {'User-Agent':f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/138.0.0.0 Safari/537.36 ({email})'
    }

# Отправляем GET-запрос к API
    response = requests.get(BASE_URL_NOMINATIM, params=params, headers=headers)

# Проверяем, что запрос выполнен успешно
    if response.status_code != 200:
        print(f"Error code: {response.status_code}")
        print(f"Error reason: {response.reason}")
        return {}

# Преобразуем ответ из JSON в Python-объект
    data = response.json()

# Если получен ровно один результат, возвращаем нужные данные
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

# Вызываем функцию и выводим результат
result = get_location_info_addr("Россия, Санкт-Петербург, Ипподромный переулок, 1 к1")
print(result)
