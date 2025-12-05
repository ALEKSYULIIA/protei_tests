import logging
import pytest
import allure
from test_params import ALL_VALID, ALL_INVALID

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestGeoCode:
    # Тесты для валидных данных (адреса и координаты вместе)
    @allure.feature('Обработка валидных данных')
    @allure.story('Адреса и координаты')
    @pytest.mark.parametrize("input_type, value", ALL_VALID)
    def test_valid_data(self, input_type, value, geo):
        if input_type == "addr":
            allure.dynamic.title(f"Тест валидного адреса: {value}")
        else:
            lat, lon = value
            allure.dynamic.title(f"Тест валидных координат: {lat}, {lon}")

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
                        "Saint Petersburg" in result["address"]
                    ), "Адрес должен содержать название Санкт-Петербурга"
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

    # Тесты для невалидных данных (адреса и координаты вместе)
    @allure.feature('Обработка невалидных данных')
    @allure.story('Адреса и координаты')
    @pytest.mark.parametrize("input_type, value", ALL_INVALID)
    def test_invalid_data(self, input_type, value, geo):
        if input_type == "addr":
            allure.dynamic.title(f"Тест невалидного адреса: {value}")
        else:
            lat, lon = value
            allure.dynamic.title(f"Тест невалидных координат: {lat}, {lon}")

        if input_type == "addr":
            address = value
            logger.info(f"Обработка невалидного адреса: {address}")
            with allure.step(f"Обработка невалидного адреса: {address}"):
                result = geo.get_location_info_addr(address)