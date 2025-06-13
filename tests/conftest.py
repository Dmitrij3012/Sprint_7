import pytest
import data
from data import Data
from methods.auth_methods import AuthMethods
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture(scope='function')
def create_test_courier():
    courier_data = Data.courier_body()
    yield courier_data
    courier_id = AuthMethods.create_id(courier_data)
    CourierMethods.delete_courier(courier_id)


@pytest.fixture(scope='function')
def create_test_courier_id():
    courier_data = Data.courier_body()
    CourierMethods.create_courier(courier_data)
    courier_id = AuthMethods.create_id(courier_data)
    yield courier_id
    CourierMethods.delete_courier(courier_id)


@pytest.fixture(scope='function')
def create_test_courier_and_order():
    courier_data = Data.courier_body()
    order_data = Data.dataset_for_order(data.COLOR[0])
    CourierMethods.create_courier(courier_data)
    order_create = OrderMethods.create_order(order_data)
    courier_id = AuthMethods.create_id(courier_data)
    track_number = order_create.json()['track']
    order_response = OrderMethods.receive_order_by_number(track_number)
    order_id = order_response.json()['order']['id']
    yield order_id, courier_id
    CourierMethods.delete_courier(courier_id)


@pytest.fixture(scope='function')
def create_test_order():
    order_data = Data.dataset_for_order(data.COLOR[0])
    order_response = OrderMethods.create_order(order_data)
    track_number = order_response.json()['track']
    yield track_number


@pytest.fixture(scope='function')
def create_courier_with_duplicate_login():
    courier_data = Data.courier_body_with_duplicate_login()
    yield courier_data
    courier_id = AuthMethods.create_id(courier_data)
    CourierMethods.delete_courier(courier_id)
