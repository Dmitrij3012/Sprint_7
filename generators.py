from faker import Faker


def courier_fake_data():
    fake = Faker('ru-RU')
    login = fake.password(length=10, special_chars=False, digits=False, upper_case=False, lower_case=True)
    password = fake.password(length=10, special_chars=False, digits=False, upper_case=False, lower_case=True)
    first_name = fake.first_name_male()
    return login, password, first_name


def order_fake_data():
    fake = Faker('ru-RU')
    name = fake.first_name_male()
    surname = fake.last_name_male()
    address = fake.street_address()
    metro = fake.random_int(1, 100)
    phone = fake.phone_number()
    rent_time = fake.random_int(1, 7)
    delivery_date = fake.date_between(start_date='today', end_date='+30d').isoformat()
    comment = fake.catch_phrase()
    return name, surname, address, metro, phone, rent_time, delivery_date, comment
