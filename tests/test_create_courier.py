import allure
import pytest
import data
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description('Создаем курьера и проверяем успешность создания')
    def test_successful_create_courier_with_all_required_fields(self, create_test_courier):
        with allure.step('Создание курьера'):
            response = CourierMethods.create_courier(create_test_courier)
        with allure.step('Проверка ответа'):
            assert response.status_code == 201
            assert response.json()['ok'] is True

    @allure.title('Возврат тела при успешном запросе')
    @allure.description('Создаем курьера и проверяем возврат тела')
    def test_successful_request_returns_response(self, create_test_courier):
        with allure.step('Создание курьера'):
            response = CourierMethods.create_courier(create_test_courier)
        with allure.step('Проверка ответа'):
            assert response.text == data.SUCCESSFUL_RESPONSE

    @allure.title('Ошибка при создании двух одинаковых курьеров')
    @allure.description('Пытаемся создать двух одинаковых курьеров и получаем ошибку')
    def test_error_its_impossible_to_create_two_identical_couriers(self, create_test_courier):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_test_courier)
        with allure.step('Попытка создания второго курьера'):
            response = CourierMethods.create_courier(create_test_courier)
        with allure.step('Проверка ответа'):
            assert response.status_code == 409
            assert response.json()['message'] == data.ERROR_MESSAGE_DUPLICATE_LOGIN_REQUEST

    @allure.title('Невозможность создания курьера с пропущенным полем')
    @allure.description('Пытаемся создать курьера с пропущенным полем и получаем ошибку')
    @pytest.mark.parametrize('body', data.BODY_WITHOUT_FIELD)
    def test_error_if_one_of_the_fields_is_missing(self, body):
        with allure.step('Создание курьера'):
            response = CourierMethods.create_courier(body)
        with allure.step('Проверка ответа'):
            assert response.status_code == 400
            assert response.json()['message'] == data.ERROR_IF_ONE_OF_THE_FIELDS_IS_MISSING

    @allure.title('Невозможность создания курьера с пустым полем')
    @allure.description('Пытаемся создать курьера с пустым полем и получаем ошибку')
    @pytest.mark.parametrize('body', data.BODY_WITH_EMPTY_FIELD)
    def test_error_if_one_of_the_fields_is_empty(self, body):
        with allure.step('Создание курьера'):
            response = CourierMethods.create_courier(body)
        with allure.step('Проверка ответа'):
            assert response.status_code == 400
            assert response.json()['message'] == data.ERROR_IF_ONE_OF_THE_FIELDS_IS_MISSING

    @allure.title('Невозможность создания курьера с повторяющимся логином')
    @allure.description('Пытаемся создать курьера с повторяющимся логином и получаем ошибку')
    def test_error_creating_courier_with_duplicate_login(self, create_courier_with_duplicate_login):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_courier_with_duplicate_login)
        with allure.step('Попытка создания курьера с повторяющимся логином'):
            response = CourierMethods.create_courier(create_courier_with_duplicate_login)
        with allure.step('Проверка ответа'):
            assert response.status_code == 409
            assert response.json()['message'] == data.ERROR_MESSAGE_DUPLICATE_LOGIN_REQUEST
