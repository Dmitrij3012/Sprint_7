import allure
import pytest
import data
from methods.order_methods import OrderMethods


class TestOrder:

    @allure.title('Успешное создание заказа')
    @allure.description('Тест проверяет успешное создание заказа без цвета, с одним цветом и с обоими цветами'
                        'и проверяет тело ответа.')
    @pytest.mark.parametrize('color', data.COLOR)
    def test_successful_order(self, color):
        with allure.step('Создание курьера и заказа'):
            response = OrderMethods.create_order(data.Data.dataset_for_order(color))
        with allure.step('Проверка ответа'):
            assert response.status_code == 201
            assert 'track' in response.text
