import pytest
from new_function_addr_coord import Nominatim

@pytest.fixture(scope="module")
def geo():
   return Nominatim()

@pytest.mark.parametrize("address", [
    # корректные адреса
    'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1',
    'Санкт-Петербург, Ипподромный переулок, 1 к1',
    'Россия, Ипподромный переулок, 1 к1',
    'Ипподромный переулок, 1 к1',
    '1 к1',
    '12345',
    'Россия, Санкт-Петербург, @#$%',
    ' ',
    '',
    'Russia, Saint-Petersburg, Ippodromniy street, 1b1',
    'Russia, Санкт-Петербург, Ипподромный переулок, 1 к1',
    'Россия, Saint-Petersburg, Ippodromniy street, 1b1',
])
def test_get_location_info_addr(address, geo):
    result = geo.get_location_info_addr(address)
    assert result is not None, "Результат не должен быть None"
    assert "Россия" in result["address"], "Адрес должен содержать 'Россия'"
    assert "Санкт-Петербург" in result["address"], "Адрес должен содержать 'Санкт-Петербург'"
    assert result["lat"] is not None, "Широта не должна быть None"
    assert result["lon"] is not None, "Долгота не должна быть None"
    assert isinstance(result["address"], str), "Адрес должен быть строкой"
    assert isinstance(result["lat"], (float, int)), "Широта должна быть числом"
    assert isinstance(result["lon"], (float, int)), "Долгота должна быть числом"
    assert result["address"].strip() != "", "Адрес не должен быть пустой строкой"


@pytest.mark.parametrize("lat, lon", [
    (60.0007332, 30.3092082),
    (.0007332, .3092082),
    (0.0007332, 0.3092082),
    (60., 30.),
    (600.0007332, 300.3092082),
    (60.0007332000, 30.3092082000),
])
def test_get_location_info_coord(lat, lon, geo):
    result = geo.get_location_info_coord(lat, lon)
    assert result is not None, "Результат не должен быть None"
    assert result["display_name"] is not None, "Адрес не должен быть None"
    assert isinstance(result["display_name"], str), "Адрес должен быть строкой"
    assert result["display_name"].strip() != "", "Адрес не должен быть пустой строкой"
