# Импортируем функцию для получения информации по адресу
from function_geocode_address import get_location_info_addr
# Импортируем функцию для получения информации по координатам
from function_geocode_coord import get_location_info_coord

# Получаем геоинформацию по адресу
result_1 = get_location_info_addr('Россия, Санкт-Петербург, Ипподромный переулок, 1 к1')
# Получаем геоинформацию по координатам: широта и долгота
result_2 = get_location_info_coord(60.0007332, 30.3092082)

# Сравниваем широту и долготу из обоих результатов
coord_equal = (result_1.get('lat') == result_2.get('lat')) and (result_1.get('lon') == result_2.get('lon'))
# Сравниваем адрес из первого результата с display_name из второго результата
address_equal = (result_1.get('address') == result_2.get('display_name'))

# Если и координаты, и адреса совпадают, выводим сообщение об идентичности результатов
if coord_equal and address_equal:
        print("Results are the same")
# Если результаты отличаются, выводим сообщение и сами результаты для анализа
else:
        print("Results are different")
        print("Address result:", result_1)
        print("Coord result:", result_2)

