import requests
from pprint import pprint


get_endpoint = 'https://httpbin.org/get'

args = {
    'fname': 'Nikolay',
    'lname': 'Ignatiev'
}
response = requests.get(get_endpoint, params=args)
print('Ответ на get-запрос')
pprint(response.json())

post_endpoint = 'https://httpbin.org/post'
args['stdnum'] = 1032172808
response = requests.post(post_endpoint, data=args)
print('Ответ на post-запрос')
pprint(response.json())

print('Задание 7')
print(response.request.method, response.request.path_url, 'HTTP/1.1')
pprint(dict(response.request.headers))
print(response.request.body)

print('Задание 10')
response = requests.post(post_endpoint, json=args)
pprint(dict(response.request.headers))
print(response.request.body)
