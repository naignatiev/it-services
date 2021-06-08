#!/bin/bash
; этот скрипт не работает, т.к результаты curl автоматически не сохраняются, надо руками копировать

ALBUM_ID=; fill pls
OWNER_ID=; fill pls
TOKEN=; fill pls
ENDPNT1="https://api.vk.com/method/photos.getUploadServer"
ENDPNT3="https://api.vk.com/method/photos.save"

curl -X GET -G $ENDPNT1 -d v=5.25 -d access_token=$TOKEN -d album_id=$ALBUM_ID
ENDPNT2=; copy here
curl -H "Content-Type: multipart/form-data" -F file1=@content/private_photo1.jpg -F file2=@content/private_photo2.jpeg -X POST $ENDPNT2 > params.json
SERVER=; copy here
HASH=; copy here
python3 help.py | curl -X GET -G $ENDPNT3 -d v=5.25 -d access_token=$TOKEN -d album_id=$ALBUM_ID -d server=$SERVER -d hash=$HASH -d "@-"s
