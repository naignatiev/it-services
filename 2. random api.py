import requests
from pprint import pprint
from time import sleep
from secret import RANDOM_ORG_TOKEN


endpoint = 'https://api.random.org/json-rpc/2/invoke'
api_key = RANDOM_ORG_TOKEN

request_data = {
    'jsonrpc': '2.0',
    'id': '42',
    'method': 'generateIntegers',
    'params': {
        'apiKey': api_key,
        'n': 5,
        'min': 2,
        'max': 3
    }
}


def get_response():
    return requests.post(endpoint, json=request_data)


def good_sleep(_response):
    if 'result' in _response.json():
        sleep(_response.json()['result']['advisoryDelay'] / 1000)
    else:
        sleep(0.5)


response = get_response()
print('Заголовок запроса')
pprint(dict(response.request.headers))

print('Тело ответа')
pprint(response.content)

print('Заголовок ответа')
pprint(dict(response.headers))


good_sleep(response)

request_data['params'] = {
    'apiKey': api_key,
    'n': 5,
    'min': 0,
    'max': 16,
    'base': 8
}

response = get_response()
print('Ответ сервера')
pprint(response.json())
print('Тип данных в JSON', type(response.json()['result']['random']['data'][0]))

good_sleep(response)
print('Неправильный ключ')
request_data['params']['apiKey'] = 'itdoesnotapikey'
response = get_response()
print(response.json()['error'])

good_sleep(response)
print('Невалидное значение')
request_data['params']['apiKey'] = api_key
request_data['params']['max'] = '1' * 200
response = get_response()
pprint(response.json()['error'])

print('Теперь последовательности')
request_data['method'] = 'generateIntegerSequences'
request_data['params']['max'] = 9
request_data['params']['length'] = 3
response = get_response()

print('Заголовок запроса')
pprint(dict(response.request.headers))

print('Заголовок ответа')
pprint(dict(response.headers))

print('Тело ответа')
pprint(response.content)
