import allure
import data
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Тест проверяет успешную авторизацию курьера с валидными учетными данными.')
    def test_successful_authorization_with_all_required_fields(self, create_test_courier):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_test_courier)
        with allure.step('Успешная авторизация'):
            response = CourierMethods.login_courier(create_test_courier)
        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'id' in response.text

    @allure.title('Возврат id при успешной авторизации')
    @allure.description('Тест проверяет возврат id при успешной авторизации.')
    def test_successful_return_a_valid_response(self, create_test_courier):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_test_courier)
        with allure.step('Успешная авторизация'):
            response = CourierMethods.login_courier(create_test_courier)
        with allure.step('Проверка ответа'):
            assert 'id' in response.text

    @allure.title('Ошибка авторизации при отсутствии поля')
    @allure.description('Тест проверяет возврат ошибки при попытке авторизации с отсутствующим полем.')
    def test_error_when_field_is_missing(self, create_test_courier):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_test_courier)
        with allure.step('Попытка авторизации'):
            body = {
                'password': create_test_courier['password']
            }
            response = CourierMethods.login_courier(body)
        with allure.step('Проверка ответа'):
            assert response.status_code == 400
            assert response.json()['message'] == data.ERROR_NOT_ENOUGH_LOGIN_DATA

    @allure.title('Ошибка авторизации при некорректном пароле')
    @allure.description('Тест проверяет возврат ошибки при попытке авторизации с некорректным паролем.')
    def test_error_with_incorrect_password(self, create_test_courier):
        with allure.step('Создание курьера'):
            CourierMethods.create_courier(create_test_courier)
        with allure.step('Попытка авторизации'):
            body = {
                'login': create_test_courier['login'],
                'password': '12345'
            }
            response = CourierMethods.login_courier(body)
        with allure.step('Проверка ответа'):
            assert response.status_code == 404
            assert response.json()['message'] == data.ERROR_ACCOUNT_NOT_FOUND
