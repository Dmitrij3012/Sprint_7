import allure
import pytest
import data
from methods.order_methods import OrderMethods


class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    @allure.description('Тест проверяет успешное принятие заказа.')
    def test_successful_accept_order(self, create_test_courier_and_order):
        with allure.step('Создание заказа и курьера'):
            order_id, courier_id = create_test_courier_and_order
            response = OrderMethods.accept_order(order_id, courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['ok'] is True

    @allure.title('Ошибка принятия заказа с отсутствующим id курьера')
    @allure.description('Тест проверяет ошибку принятия заказа с отсутствующим id курьера.')
    def test_error_order_without_courier_id(self, create_test_courier_and_order):
        with allure.step('Создание заказа и курьера. Передача пустого id курьера'):
            order_id, courier_id = create_test_courier_and_order
            response = OrderMethods.accept_order(order_id, '')
        with allure.step('Проверка ответа'):
            assert response.status_code == 400
            assert response.json()['message'] == data.ERROR_NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Ошибка принятия заказа с некорректным id курьера')
    @allure.description('Тест проверяет ошибку принятия заказа с некорректным id курьера.')
    @pytest.mark.parametrize('invalid_courier_id', data.INVALID_ID)
    def test_error_order_with_invalid_courier_id(self, create_test_courier_and_order, invalid_courier_id):
        with allure.step('Создание заказа и курьера. Передача некорректного id курьера'):
            order_id, courier_id = create_test_courier_and_order
            response = OrderMethods.accept_order(order_id, invalid_courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_COURIER_WITH_SUCH_ID_DOES_NOT_EXIST

    @allure.title('Ошибка принятия заказа с отсутствующим id заказа')
    @allure.description('Тест проверяет ошибку принятия заказа с отсутствующим id заказа.')
    def test_error_order_without_order_id(self, create_test_courier_and_order):
        with allure.step('Создание заказа и курьера. Передача пустого id заказа'):
            order_id, courier_id = create_test_courier_and_order
            response = OrderMethods.accept_order('', courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_NOT_FOUND

    @allure.title('Ошибка принятия заказа с некорректным id заказа')
    @allure.description('Тест проверяет ошибку принятия заказа с некорректным id заказа.')
    @ pytest.mark.parametrize('invalid_order_id', data.INVALID_ID)
    def test_error_order_with_invalid_order_id(self, create_test_courier_and_order, invalid_order_id):
        with allure.step('Создание заказа и курьера. Передача некорректного id заказа'):
            order_id, courier_id = create_test_courier_and_order
            response = OrderMethods.accept_order(invalid_order_id, courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_ORDER_WITH_SUCH_ID_DOES_NOT_EXIST
