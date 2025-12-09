import pytest

# Адреса валидные
VALID_ADDR = [
    pytest.param("addr", 'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1', id="valid_addr_1"),
    pytest.param("addr", 'Russia, Санкт-Петербург, Ипподромный переулок, 1 к1', id="valid_addr_2"),
    pytest.param("addr", 'Russia, Saint-Petersburg', id="valid_addr_3"),
    pytest.param("addr", 'Россия, Saint-Petersburg, Невский проспект', id="valid_addr_4"),
]
# Адреса невалидные
INVALID_ADDR = [
    pytest.param("addr", 'Ипподромный переулок, 1 к1', id="invalid_addr_1"),
    pytest.param("addr", '1 к1', id="invalid_addr_2"),
    pytest.param("addr", '12345', id="invalid_addr_3"),
    pytest.param("addr", 'Россия, Санкт-Петербург, @#$%', id="invalid_addr_4"),
    pytest.param("addr", ' ', id="invalid_addr_5"),
    pytest.param("addr", '', id="invalid_addr_6"),
    pytest.param("addr", None, id="invalid_addr_7"),
]
# Координаты валидные
VALID_COORD = [
    pytest.param("coord", (60.0007332, 30.3092082), id="valid_coord_1"),
    pytest.param("coord", (60., 30.), id="valid_coord_2"),
    pytest.param("coord", ("60.0007332000", "30.3092082000"), id="valid_coord_3"),
]
# Координаты невалидные
INVALID_COORD = [
    pytest.param("coord", (".0007332", ".3092082"), id="invalid_coord_1"),
    pytest.param("coord", (600.0, 300.0), id="invalid_coord_2"),
    pytest.param("coord", (-100.0, 200.0), id="invalid_coord_3"),
    pytest.param("coord", (0.0007332, 0.3092082), id="invalid_coord_4"),
    pytest.param("coord", (None, None), id="invalid_coord_5"),
]

# Все валидные адреса + координаты
ALL_VALID = VALID_ADDR + VALID_COORD

# Все невалидные адреса + координаты
ALL_INVALID = INVALID_ADDR + INVALID_COORD