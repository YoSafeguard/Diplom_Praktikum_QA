# Заголовок
headers = {
    "Content-Type": "application/json",
}

# Тело запроса для создания заказа
order_body = {
    "firstName": "Юрий",
    "lastName": "Куклин",
    "address": "Арбат, д. 16 кв. 22",
    "metroStation": 162,
    "phone": "+7 999 355 35 35",
    "rentTime": 1,
    "deliveryDate": "2024-08-20",
    "comment": "Эх, прокачусь!",
    "color": [
        "BLACK"
    ]
}

# Параметры для поиска заказа по номеру трека
parameter_get = {
    "t": ""
}