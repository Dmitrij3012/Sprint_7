import allure
import pytest
import data
from methods.order_methods import OrderMethods


class TestReceivingOrder:

    @allure.title('Успешное получение заказа по номеру')
    @allure.description('Тест проверяет получение заказа по номеру.')
    def test_successful_receive_order_by_number(self, create_test_order):
        with allure.step('Создание заказа. Получение по номеру'):
            response = OrderMethods.receive_order_by_number(create_test_order)
        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'id' in response.json()['order']

    @allure.title('Ошибка получения заказа с отсутствующим номером')
    @allure.description('Тест проверяет ошибку получения заказа с отсутствующим номером.')
    def test_error_request_without_number(self, create_test_order):
        with allure.step('Создание заказа. Передача пустого номера'):
            response = OrderMethods.receive_order_by_number('')
        with allure.step('Проверка ответа'):
            assert response.status_code == 400
            assert response.json()['message'] == data.ERROR_NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Ошибка получения заказа с некорректным номером')
    @allure.description('Тест проверяет ошибку получения заказа с некорректным номером')
    @pytest.mark.parametrize('invalid_order_number', data.INVALID_ID)
    def test_error_request_with_invalid_number(self, create_test_order, invalid_order_number):
        with allure.step('Создание заказа. Передача некорректного номера'):
            response = OrderMethods.receive_order_by_number(invalid_order_number)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_ORDER_NOT_FOUND
