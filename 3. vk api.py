import requests
from pprint import pprint
from time import sleep
from secret import VK_TOKEN

access_token = VK_TOKEN
users_search_endpoint = 'https://api.vk.com/method/users.search'
OWNER_ID = 1

params = {
    'access_token': access_token,
    'v': 5.25,
    'q': 'Николай Дуров',
    'sort': 1,
    'count': 2,
    'fields': 'education,about'
}


response = requests.get(users_search_endpoint, params=params)
pprint(response.json())

print('Страна')
endpoint = 'https://api.vk.com/method/database.getCountries'
params = {
    'access_token': access_token,
    'v': 5.25,
    'code': 'RU'
}
response = requests.get(endpoint, params=params)
pprint(response.json())

print('Город')
endpoint = 'https://api.vk.com/method/database.getCities'
params = {
    'access_token': access_token,
    'v': 5.25,
    'country_id': 1,
    'code': 'великие лу'
}
response = requests.get(endpoint, params=params)
pprint(response.json())

print('Школа')
endpoint = 'https://api.vk.com/method/database.getSchools'
params = {
    'access_token': access_token,
    'v': 5.25,
    'city_id': 34,
    'q': 'гимназия'
}
response = requests.get(endpoint, params=params)
pprint(response.json())

print('Университет')
endpoint = 'https://api.vk.com/method/database.getUniversities'
params = {
    'access_token': access_token,
    'v': 5.25,
    'country_id': 1,
    'city_id': 1,
    'q': 'РУДН'
}
response = requests.get(endpoint, params=params)
pprint(response.json())


sleep(1)
print('Список документов')
endpoint = 'https://api.vk.com/method/docs.get'
params = {
    'access_token': access_token,
    'v': 5.25,
    'count': 2,
    'owner_id': OWNER_ID
}
response = requests.get(endpoint, params=params)
pprint(response.json())


sleep(1)
endpoint = 'https://api.vk.com/method/docs.getUploadServer'
response = requests.get(endpoint, params={'access_token': access_token, 'v': 5.25})
with open('content/text_file.txt', 'rb') as f:
    response = requests.post(response.json()['response']['upload_url'], files={'file': ('text_file.txt', f)})
params = {
    'access_token': access_token,
    'v': 5.25,
    'file': response.json()['file'],
    'owner_id': OWNER_ID
}
response = requests.get('https://api.vk.com/method/docs.save', params=params)

sleep(1)
print('Альбомы')
endpoint = 'https://api.vk.com/method/photos.getAlbums'
response = requests.get(endpoint, params={'access_token': access_token, 'v': 5.25, 'owner_id': OWNER_ID})
pprint(response.json())
