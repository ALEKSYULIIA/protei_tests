import pytest
from new_function_addr_coord import Nominatim

@pytest.fixture(scope="module")
def geo():
   return Nominatim()

# Позитивные проверки адреса: ожидаем, что найдется Россия/Russia, Санкт-Петербург/Saint-Petersburg
'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1',
'Russia, Санкт-Петербург, Ипподромный переулок, 1 к1',
'Russia, Saint-Petersburg, Ippodromniy street, 1b1',
'Россия, Saint-Petersburg, Ippodromniy street, 1b1',

# Негативные проверки адреса
'Ипподромный переулок, 1 к1',
'1 к1',
'12345',
'Россия, Санкт-Петербург, @#$%',
' ',
'',
]

@pytest.mark.parametrize("address")
def test_get_location_info_addr(address, geo):
    result = geo.get_location_info_addr(address)
    assert result is not None, "Результат не должен быть None"
    assert result["lat"] is not None, "Широта не должна быть None"
    assert result["lon"] is not None, "Долгота не должна быть None"
    assert "Россия" in result["address"] or "Russia" in result[
        "address"], "Адрес должен содержать 'Россия' или 'Russia'"
    assert "Санкт-Петербург" in result["address"] or "Saint Petersburg" in result[
        "address"], "Адрес должен содержать 'Санкт-Петербург' или 'Saint Petersburg'"
    assert isinstance(result, dict), "Результат должен быть словарём"
    assert "address" in result, "Должно быть поле 'address'"
    assert "lat" in result, "Должно быть поле 'lat'"
    assert "lon" in result, "Должно быть поле 'lon'"
    assert result["address"].strip() != "", "Адрес не должен быть пустой строкой"
    assert isinstance(result["address"], str), "Адрес должен быть строкой"
    assert isinstance(result["lat"], (float, int)), "Широта должна быть числом"
    assert isinstance(result["lon"], (float, int)), "Долгота должна быть числом"


# Позитивные проверки адреса по координатам: ожидаем, что найдется Санкт-Петербург
(60.0007332, 30.3092082),
(60., 30.),
(60.0007332000, 30.3092082000),

# Негативные проверки адреса по координатам
(.0007332, .3092082),
(600.0, 300.0),
(-100.0, 200.0),
(0.0007332, 0.3092082),

@pytest.mark.parametrize("lat, lon")
def test_get_location_info_coord(lat, lon, geo):
    result = geo.get_location_info_coord(lat, lon)
    assert result is not None, "Результат не должен быть None"
    assert result["display_name"] is not None, "Адрес не должен быть None"
    assert isinstance(result["display_name"], str), "Адрес должен быть строкой"
    assert result["display_name"].strip() != "", "Адрес не должен быть пустой строкой"




