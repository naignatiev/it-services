#!/bin/bash
; этот скрипт не работает, т.к результаты curl автоматически не сохраняются, надо руками копировать

OWNER_ID=; fill pls
ENDPNT1="https://api.vk.com/method/docs.getUploadServer"
ENDPNT3="https://api.vk.com/method/docs.save"
TOKEN=; fill pls

curl -X GET -G $ENDPNT1 -d v=5.25 -d access_token=$TOKEN
ENDPNT2=; copy result here
curl -H "Content-Type: multipart/form-data" -F file=@content/text_file.txt -X POST $ENDPNT2
FILE=; fill
curl -X GET -G $ENDPNT3 -d v=5.25 -d access_token=$TOKEN -d owner_id=$OWNER_ID -d file=$FILE
