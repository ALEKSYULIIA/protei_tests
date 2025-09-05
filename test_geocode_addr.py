import pytest

from function_geocode_address import get_location_info_addr

def test_get_location_info_addr():
    address = 'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1'
    result = get_location_info_addr(address)
    assert result is not None, "Результат не должен быть None"
    assert "Россия" in result["address"], "Адрес должен содержать 'Россия'"
    assert "Санкт-Петербург" in result["address"], "Адрес должен содержать 'Санкт-Петербург'"
    assert result["lat"] is not None, "Широта не должна быть None"
    assert result["lon"] is not None, "Долгота не должна быть None"