import requests
import url


class OrderMethods:

    @staticmethod
    def create_order(body):
        return requests.post(f'{url.URL}{url.ORDERS}', json=body)

    @staticmethod
    def orders_list():
        return requests.get(f'{url.URL}{url.ORDERS}')

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(f'{url.URL}{url.ACCEPT_ORDER}{order_id}?courierId={courier_id}')

    @staticmethod
    def receive_order_by_number(track_number):
        return requests.get(f'{url.URL}{url.RECEIVE_ORDER}?t={track_number}')
