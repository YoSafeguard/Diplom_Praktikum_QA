# Импорт путей  из configuration.py,
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из data.py, в котором содержаться заголовки и тело запроса
import data

# Функция для отправки POST-запроса для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVER + configuration.URL_CREATE_ORDER,
                         json=body)

# Функция с телом запроса для создания нового заказа
order_response = post_new_order(data.order_body)


# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVER+configuration.URL_GET_ORDER,
                        params=track_order)