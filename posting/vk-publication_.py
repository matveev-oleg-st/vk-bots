#!/usr/bin/env python3

import requests
import json

vk_api_version = "5.103"
vk_api_url     = "https://api.vk.com/method/"
vk_app_id      = "7858688"
vk_group_id    = "204666028"
vk_token       = "855e549d415f2179e4cc9521272972f374fb5e3b6fc16a2b78e96910e189f91fc1e410ec2d111e4b8ff2b"
vk_token2      = "df4f9b459686bd5df4c4bfc4daf86fda35b0f6b59dee624a0fdf7f6d2e96018f09d9b064b0dd4650feadc"
vk_from_group  = "1"

vk_url         = vk_api_url + "wall.post"

vk_attachments = {
                'type': 'link',
                'url': 'https://api.vk.com',
                'title': 'title',
                'description': 'description',
                'image_src': '',
                'preview_page': '',
                'preview_url': ''
}
    
vk_params      = {
                'owner_id': vk_group_id,
                'from_group': vk_from_group,
                'attachments': vk_attachments,
                'v': vk_api_version,
                'access_token': vk_token2
                }

vk_response    = requests.get(vk_url, params=vk_params)#.json()['response']['items']
print(vk_response.text)


#vk_attachments = "attachments=" + "type:'link',url:https://api.vk.com,title:'title'"    
#vk_attachment = (
#    ('url', 'https://vk.com/dev/objects/link'),
#    ('title', 'title'),
#    ('description', 'description')
#)
#vk_attachmen  = "<HTTPS><example.ru>"
#vk_att        = "{'url': 'https://api.vk.com','title': 'title','description': 'description'}"
#vk_params     = (
#    ('v', vk_version),
#    ('access_token', vk_token),
#    ('owner_id', vk_group_id),
#    ('attachments', vk_att),
#    ('friends_only', 0),
#    ('from_group', 1)
#)

#('message', vk_message),
#vk_message    = "https://qna.habr.com/q/648070"

#, {"type": "audio", "audio": {audio}}]
#{"peer_id": id, "message":"Привет!!!", "random_id":123456}
#vk_content    = 'message' +'Hello world <a href="#">sfsf</a>'
#vk_content    = 'attachments=' + '{"type": "link", "url": "https://api.vk.com", "title": "title", "description": "description" }'
#"message=" + "hello..." + "&

#vk_content    = "attachments=" + "type:link,url:https://api.vk.com,title:title"

#vk_url        = "https://api.vk.com/method/wall.post?owner_id=-" + vk_group_id + "&form_group=1&scope=wall&" + vk_content + "&v=5.130&access_token=" + vk_token2
#vk_response   = requests.get(vk_url)
#print(vk_response.text)
