import json

with open('params.json') as f:
    data = json.load(f)

print('photos_list=', data['photos_list'], sep='')
