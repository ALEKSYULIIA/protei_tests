import pytest
from new_function_addr_coord import Nominatim

@pytest.fixture(scope="module")
def geo():
   return Nominatim()

# Позитивные проверки адреса: ожидаем, что найдется Россия/Russia, Санкт-Петербург/Saint-Petersburg
VALID_ADDRESS = [
'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1',
'Russia, Санкт-Петербург, Ипподромный переулок, 1 к1',
'Russia, Saint-Petersburg, Ippodromniy street, 1b1',
'Россия, Saint-Petersburg, Ippodromniy street, 1b1',
]

# Негативные проверки адреса
INVALID_ADDRESS = [
'Ипподромный переулок, 1 к1',
'1 к1',
'12345',
'Россия, Санкт-Петербург, @#$%',
' ',
'',
]

@pytest.mark.parametrize("address", VALID_ADDRESS)
def test_get_location_info_valid_addr(address, geo):
    result = geo.get_location_info_addr(address)
    assert result is not None, "Результат не должен быть None"
    assert isinstance(result, dict), "Результат должен быть словарём"
    assert "Россия" in result["address"] or "Russia" in result[
        "address"], "Адрес должен содержать 'Россия' или 'Russia'"
    assert (
            "Санкт-Петербург" in result["address"] or
            "Saint-Petersburg" in result["address"] or
            "Санкт Петербург" in result["address"] or
            "Saint Petersburg" in result["address"]),\
        "Адрес должен содержать название Санкт-Петербурга"


@pytest.mark.parametrize("address", INVALID_ADDRESS)
def test_get_location_info_invalid_addr(address, geo):
    result = geo.get_location_info_addr(address)
    if result is not None:
        assert isinstance(result["addressall"], str), "Адрес должен быть строкой"
        assert isinstance(result, dict), "Результат должен быть словарём"



SPB_COORDINATES = [
# Позитивные проверки адреса по координатам: ожидаем, что найдется Санкт-Петербург
(60.0007332, 30.3092082),
(60., 30.),
(60.0007332000, 30.3092082000),
]

NO_SPB_COORDINATES = [
# Негативные проверки адреса по координатам
(.0007332, .3092082),
(600.0, 300.0),
(-100.0, 200.0),
(0.0007332, 0.3092082),
]


@pytest.mark.parametrize("lat, lon", SPB_COORDINATES)
def test_get_location_info_valid_coord(lat, lon, geo):
    result = geo.get_location_info_coord(lat, lon)
    assert result is not None, "Результат не должен быть None"
    assert result["display_name"] is not None, "Адрес не должен быть None"
    assert result["display_name"].strip() != "", "Адрес не должен быть пустой строкой"


@pytest.mark.parametrize("lat, lon", NO_SPB_COORDINATES)
def test_get_location_info_invalid_coord(lat, lon, geo):
    result = geo.get_location_info_coord(lat, lon)
    if result is not None:
        assert isinstance(result, dict), "Результат должен быть словарём"
        assert isinstance(result.get("display_name", ""), str), "Адрес должен быть строкой"




