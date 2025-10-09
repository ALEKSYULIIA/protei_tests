import logging
import pytest
from new_function_addr_coord import Nominatim
import allure

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@pytest.fixture(scope="module")
def geo():
   return Nominatim()

VALID_CASES = [
    # Адреса
    pytest.param("addr", 'Россия, Санкт-Петербург, Ипподромный переулок, 1 к1', id="valid_addr_1"),
    pytest.param("addr", 'Russia, Санкт-Петербург, Ипподромный переулок, 1 к1', id="valid_addr_2"),
    pytest.param("addr", 'Russia, Saint-Petersburg', id="valid_addr_3"),
    pytest.param("addr", 'Россия, Saint-Petersburg, Невский проспект', id="valid_addr_4"),
    # Координаты
    pytest.param("coord", (60.0007332, 30.3092082), id="valid_coord_1"),
    pytest.param("coord", (60., 30.), id="valid_coord_2"),
    pytest.param("coord", ("60.0007332000", "30.3092082000"), id="valid_coord_3"),
]

INVALID_CASES = [
    # Адреса
    pytest.param("addr", 'Ипподромный переулок, 1 к1', id="invalid_addr_1"),
    pytest.param("addr", '1 к1', id="invalid_addr_2"),
    pytest.param("addr", '12345', id="invalid_addr_3"),
    pytest.param("addr", 'Россия, Санкт-Петербург, @#$%', id="invalid_addr_4"),
    pytest.param("addr", ' ', id="invalid_addr_5"),
    pytest.param("addr", '', id="invalid_addr_6"),
    # Координаты
    pytest.param("coord", (".0007332", ".3092082"), id="invalid_coord_1"),
    pytest.param("coord", (600.0, 300.0), id="invalid_coord_2"),
    pytest.param("coord", (-100.0, 200.0), id="invalid_coord_3"),
    pytest.param("coord", (0.0007332, 0.3092082), id="invalid_coord_4"),
]
@allure.feature('Обработка валидных адреса и координат')
@pytest.mark.parametrize("input_type, value", VALID_CASES)
def test_valid_addr_coord(input_type, value, geo):
        if input_type == "addr":
            address = value
            logger.info(f"Обработка валидного адреса: {address}")
            with allure.step(f"Обработка валидного адреса: {address}"):
                result = geo.get_location_info_addr(address)
                logger.debug(f"Получен результат: {result}")
                with allure.step("Проверка наличия результата (не None)"):
                    assert result is not None, "Результат не должен быть None"
                with allure.step("Проверка типа данных результата (должен быть словарём)"):
                    assert isinstance(result, dict), "Результат должен быть словарём"
                with allure.step("Проверка наличия в результате ключа 'address'"):
                    assert "address" in result, "В результате должен быть ключ 'address'"
                with allure.step("Проверка наличия в результате ключей 'lat' и 'lon'"):
                    assert "lat" in result and "lon" in result, "В результате должны быть ключи 'lat' и 'lon'"
                with allure.step("Проверка наличия адреса в результате (адрес не должен быть пустой строкой)"):
                    assert result["address"].strip() != "", "Адрес не должен быть пустым"
                with allure.step("Проверка типа данных адреса в результате (должен быть строкой)"):
                    assert isinstance(result["address"], str), "Адрес должен быть строкой"
                with allure.step("Проверка наличия в адресе 'Россия' или 'Russia'"):
                    assert "Россия" in result["address"] or "Russia" in result[
                "address"], "Адрес должен содержать 'Россия' или 'Russia'"
                with allure.step("Проверка наличия в адресе названия Санкт-Петербурга"):
                    assert (
                    "Санкт-Петербург" in result["address"] or
                    "Saint-Petersburg" in result["address"] or
                    "Санкт Петербург" in result["address"] or
                    "Saint Petersburg" in result["address"]), \
                "Адрес должен содержать название Санкт-Петербурга"
        elif input_type == "coord":
            lat, lon = value
            logger.info(f"Обработка валидных координат: {lat}, {lon}")
            with allure.step(f"Обработка валидных координат: {lat}, {lon}"):
                result = geo.get_location_info_coord(lat, lon)
                logger.debug(f"Получен результат: {result}")
                with allure.step("Проверка наличия результата (не None)"):
                    assert result is not None, "Результат не должен быть None"
                with allure.step("Проверка наличия адреса в результате (не None)"):
                    assert result["display_name"] is not None, "Адрес не должен быть None"
                with allure.step("Проверка наличия адреса в результате (адрес не должен быть пустой строкой)"):
                    assert result["display_name"].strip() != "", "Адрес не должен быть пустой строкой"

@allure.feature('Обработка невалидных адреса и координат')
@pytest.mark.parametrize("input_type, value", INVALID_CASES)
def test_invalid_addr_coord(input_type, value, geo):
    if input_type == "addr":
        address = value
        logger.info(f"Обработка невалидного адреса: {address}")
        with allure.step(f"Обработка невалидного адреса: {address}"):
            result = geo.get_location_info_addr(address)
            logger.debug(f"Получен результат: {result}")
            with allure.step("Проверка, что результат отсутствует (None) или представлен в виде словаря"):
                assert result is None or isinstance(result, dict), "Результат должен быть словарём или None"
            if result is not None:
                with allure.step("Проверка, что результат отсутствует (None) или представлен в виде строки"):
                    assert result.get("address") is None or isinstance(result.get("address"), str), "Адрес должен быть строкой или None"
    elif input_type == "coord":
        lat, lon = value
        logger.info(f"Обработка невалидных координат: {lat}, {lon}")
        with allure.step(f"Обработка невалидных координат: {lat}, {lon}"):
            result = geo.get_location_info_coord(lat, lon)
            logger.debug(f"Получен результат: {result}")
            with allure.step("Проверка, что результат отсутствует (None) или представлен в виде словаря"):
                assert result is None or isinstance(result, dict), "Результат должен быть None или словарём"
            if result is not None:
                display_name = result.get("display_name")
                with allure.step("Проверка, что результат отсутствует (None) или представлен в виде строки"):
                    assert display_name is None or isinstance(display_name, str), "Адрес должен быть строкой или None"