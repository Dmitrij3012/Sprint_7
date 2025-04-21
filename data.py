import generators


class Data:

    @staticmethod
    def courier_body():
        login, password, first_name = generators.courier_fake_data()
        return {
            'login': login,
            'password': password,
            'firstName': first_name
        }

    @staticmethod
    def courier_body_with_duplicate_login():
        login, password, first_name = generators.courier_fake_data()
        return {
            'login': '777test_123_456',
            'password': password,
            'firstName': first_name
        }

    @staticmethod
    def dataset_for_order(color):
        name, surname, address, metro, phone, rent_time, delivery_date, comment = generators.order_fake_data()
        return {
            "firstName": name,
            "lastName": surname,
            "address": address,
            "metroStation": metro,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": [
                f'{color}'
            ]
        }


COLOR = ('BLACK', 'GREY', ['BLACK, GREY'], '')

ERROR_MESSAGE_DUPLICATE_LOGIN_REQUEST = 'Этот логин уже используется. Попробуйте другой.'
ERROR_IF_ONE_OF_THE_FIELDS_IS_MISSING = 'Недостаточно данных для создания учетной записи'
ERROR_NOT_ENOUGH_LOGIN_DATA = 'Недостаточно данных для входа'
ERROR_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
ERROR_NOT_FOUND = 'Not Found.'
ERROR_COURIER_WITH_THIS_ID_NO = 'Курьера с таким id нет.'
ERROR_NOT_ENOUGH_DATA_TO_SEARCH = 'Недостаточно данных для поиска'
ERROR_COURIER_WITH_SUCH_ID_DOES_NOT_EXIST = 'Курьера с таким id не существует'
ERROR_ORDER_WITH_SUCH_ID_DOES_NOT_EXIST = 'Заказа с таким id не существует'
ERROR_ORDER_NOT_FOUND = 'Заказ не найден'
SUCCESSFUL_RESPONSE = '{"ok":true}'


BODY_WITHOUT_FIELD = (
    {
        'password': Data.courier_body()['password'],
        'firstName': Data.courier_body()['firstName']
    },
    {
        'login': Data.courier_body()['login'],
        'firstName': Data.courier_body()['firstName']
    },
    {
        'login': Data.courier_body()['login'],
        'password': Data.courier_body()['password']
    }
)

BODY_WITH_EMPTY_FIELD = (
    {
        'login': '',
        'password': Data.courier_body()['password'],
        'firstName': Data.courier_body()['firstName']
    },
    {
        'login': Data.courier_body()['login'],
        'password': '',
        'firstName': Data.courier_body()['firstName']
    },
    {
        'login': Data.courier_body()['login'],
        'password': Data.courier_body()['password'],
        'firstName': ''
    }
)

INVALID_ID = ('99999999', 99999999)
