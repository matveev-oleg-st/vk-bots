#!/usr/bin/env python3

import vk_api



#для того чтобы получить token cоздаёшь своё приложения переходишь по ссылке, не забывая после client_id указать id приложения, указывая необходимые права (тут лишние)
#https://oauth.vk.com/authorize?client_id=1&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos,video,audio,groups,wall,messages&response_type=token&v=5.92&state=123456
#разрешаешь доступ и тебя перекидывать на страницу где в ссылке на страницу есть access_token который тебе и нужен

#vk_group_id = int(owner_id)
#, 'message': "your_message"}
#vk_attachments = "'type':'link','url':'https://api.vk.com','title':'title','description':'description','image_src':'','preview_page':'', 'preview_url':''"
#'attachments': vk_attachments

vk_login       = 'matveev.oleg.st@gmail.com'
vk_password    = 'glize2020'
vk_token       = "df4f9b459686bd5df4c4bfc4daf86fda35b0f6b59dee624a0fdf7f6d2e96018f09d9b064b0dd4650feadc"
vk_method      = 'wall.post'
vk_group_id    = 204666028

vk_message     = "== Раздел статьи =="
vk_data        = {'owner_id':vk_group_id,'from_group':'1','message': vk_message}

vk = vk_api.VkApi(login=vk_login, password=vk_password, token=vk_token)
vk.method(vk_method, vk_data)
