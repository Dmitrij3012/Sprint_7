import allure
from methods.order_methods import OrderMethods


class TestListOrders:

    @allure.title('Успешный возврат списка заказов')
    @allure.description('Тест проверяет успешный возврат списка заказов.')
    def test_successful_return_order_list(self):
        with allure.step('Возврат списка заказов'):
            response = OrderMethods.orders_list()
        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'id' and 'courierId' in response.text
