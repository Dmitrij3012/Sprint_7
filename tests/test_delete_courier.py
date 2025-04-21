import allure
import pytest
import data
from methods.courier_methods import CourierMethods


class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    @allure.description('Тест проверяет успешное удаление курьера.')
    def test_successful_delete_courier(self, create_test_courier_id):
        with allure.step('Создание и удаление курьера'):
            response = CourierMethods.delete_courier(create_test_courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['ok'] is True

    @allure.title('Возврат тела при успешном запросе')
    @allure.description('Тест проверяет возврат тела при успешном запросе.')
    def test_successful_request_returns_response(self, create_test_courier_id):
        with allure.step('Создание и удаление курьера'):
            response = CourierMethods.delete_courier(create_test_courier_id)
        with allure.step('Проверка ответа'):
            assert response.text == data.SUCCESSFUL_RESPONSE

    @allure.title('Ошибка удаления при отсутствии id')
    @allure.description('Тест проверяет ошибку удаления курьера при отсутствии id.')
    def test_error_without_id(self, create_test_courier_id):
        with allure.step('Создание и попытка удаления курьера с отсутствующим id'):
            response = CourierMethods.delete_courier('')
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_NOT_FOUND

    @allure.title('Ошибка удаления при некорректном id')
    @allure.description('Тест проверяет ошибку удаления курьера при некорректном id.')
    @pytest.mark.parametrize('invalid_courier_id', data.INVALID_ID)
    def test_error_with_invalid_id(self, create_test_courier_id, invalid_courier_id):
        with allure.step('Создание и попытка удаления курьера с некорректным id'):
            response = CourierMethods.delete_courier(invalid_courier_id)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_COURIER_WITH_THIS_ID_NO
