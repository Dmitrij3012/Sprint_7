import requests
import url


class AuthMethods:
    @staticmethod
    def create_id(body):
        response = requests.post(f'{url.URL}{url.LOGIN_COURIER}', json=body)
        return response.json()['id']
