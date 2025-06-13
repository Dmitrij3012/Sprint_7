import requests
import url


class CourierMethods:

    @staticmethod
    def create_courier(body):
        return requests.post(f'{url.URL}{url.COURIER}', json=body)

    @staticmethod
    def login_courier(body):
        return requests.post(f'{url.URL}{url.LOGIN_COURIER}', json=body)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{url.URL}{url.COURIER}{courier_id}')
