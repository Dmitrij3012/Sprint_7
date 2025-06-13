#### <h1>Финальный проект 7 спринта</h1>
<hr>

#### <h3>Студент: Дмитрий Соловьев</h2>
#### <h3>Когорта: #18</h2>
<hr>

#### <h1>Тестирование Яндекс Самокат</h1>

#### <h2>Инструкция по запуску:</h>

### 1. Установить зависимости:

> pip install -r requirements.txt</h>

### 2. Запустить все тесты и записать отчет:

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по тестированию</h>

> allure serve ./allure-results

<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла                                                               | Содержание файла                 |
|------------------------------------------------------------------------------|----------------------------------|
| [allure_results](allure_results)                                             | Папка с отчетами Allure          | 
| [methods](methods)                                                           | Папка с методами                 |
| [tests](tests)                                                               | Папка с тестами                  |
| [test_create_courier.py](tests/test_create_courier.py)                       | Тесты создания курьера           |
| [test_login_courier.py](tests/test_login_courier.py)                         | Тесты авторизации курьера        |
| [test_create_order.py](tests/test_create_order.py)                           | Тесты создания заказа            |
| [test_list_orders.py](tests/test_list_orders.py)                             | Тест получения списка заказов    |
| [test_delete_courier.py](tests/test_delete_courier.py)                       | Тесты удаления курьера           |
| [test_accept_order.py](tests/test_accept_order.py)                           | Тесты принятия заказа            |
| [test_receiving_order_by_number.py](tests/test_receiving_order_by_number.py) | Тесты получения заказа по номеру |
| [auth_methods.py](methods/auth_methods.py)                                   | Метод получения id               |
| [courier_methods.py](methods/courier_methods.py)                             | Методы для работы с курьерами    |
| [order_methods.py](methods/order_methods.py)                                 | Методы для работы с заказами     |
| [conftest.py](tests/conftest.py)                                             | Фикстуры                         |
| [generators.py](generators.py)                                               | Генераторы данных                |
| [data.py](data.py)                                                           | Файл с данными                   |
| [url.py](url.py)                                                             | Файл с URL                       |
| [requirements.txt](requirements.txt)                                         | Файл с зависимостями             |
