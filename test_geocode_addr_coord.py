import pytest
from new_function_addr_coord import Nominatim

def test_get_location_info_addr():
    geo = Nominatim()
    address = 'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1'
    result = geo.get_location_info_addr(address)
    assert result is not None, "Результат не должен быть None"
    assert "Россия" in result["address"], "Адрес должен содержать 'Россия'"
    assert "Санкт-Петербург" in result["address"], "Адрес должен содержать 'Санкт-Петербург'"
    assert result["lat"] is not None, "Широта не должна быть None"
    assert result["lon"] is not None, "Долгота не должна быть None"

def test_get_location_info_coord():
    geo = Nominatim()
    lat = 60.0007332
    lon = 30.3092082
    result = geo.get_location_info_coord(lat, lon)
    assert result is not None, "Результат не должен быть None"
    assert result["display_name"] is not None, "Адрес не должен быть None"


