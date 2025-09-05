import pytest
from function_geocode_coord import get_location_info_coord

def test_get_location_info_coord():
    lat = 60.0007332
    lon = 30.3092082
    result = get_location_info_coord(lat, lon)
    assert result is not None, "Результат не должен быть None"
    assert result["display_name"] is not None, "Адрес не должен быть None"


