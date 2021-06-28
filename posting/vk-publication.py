#!/usr/bin/env python3

import requests

vk_api_version = "5.103"
vk_api_url     = "https://api.vk.com/method/"
vk_app_id      = "7858688"
vk_app_key     = "Eoc81FQFIaGb3mGTVUhy"
vk_app_key2    = "d9033f9cd9033f9cd9033f9cabd974d59cdd903d9033f9cb9a609ef8c6bcb0e695d3149"
vk_group_id    = "-204666028"
vk_token       = "855e549d415f2179e4cc9521272972f374fb5e3b6fc16a2b78e96910e189f91fc1e410ec2d111e4b8ff2b"
vk_token2      = "df4f9b459686bd5df4c4bfc4daf86fda35b0f6b59dee624a0fdf7f6d2e96018f09d9b064b0dd4650feadc"
vk_from_group  = "1"

vk_method      = "wall.post"
vk_url         = vk_api_url + vk_method

vk_message     = "Hello world!!!\nsdfsf\n#новости"
vk_post        = {'link': 'http://example.com/some-page.html','text': 'hello world'}
vk_attachments = []
vk_attachments.append(vk_post.get('link'))

#vk_response    = requests.post(vk_url, params={
#	'owner_id': vk_group_id,
#	'from_group': vk_from_group,
#	'message': vk_message,
#	'attachments': vk_attachments,
#    'v': vk_api_version,
#	'access_token': vk_token2
#})

vk_url         = 'https://oauth.vk.com/access_token?client_id=' + vk_app_id + '&client_secret=' + vk_app_key + '&redirect_uri=https://discurs.info&code=' + vk_token
vk_response    = requests.get(vk_url)
print(vk_response.text)

#------------------------------------------

#https://vk.com/editapp?id=7858688&section=options
#https://oauth.vk.com/access_token?client_id=7858688&client_secret=Eoc81FQFIaGb3mGTVUhy&v=5.130&grant_type=client_credentials
#access_token  = 'e5aace30e5aace30e5f12ecfb5e5dd2430ee5aae5aace30850c8f6bd219f704870558c2'
#https://oauth.vk.com/authorize?client_id=7858688&display=page&redirect_uri=http://discurs.info/&scope=friends&response_type=code&v=5.130
#https://oauth.vk.com/authorize?client_id=7858688&display=page&redirect_uri=http://discurs.info/callback&scope=friends&response_type=code&v=5.130
https://oauth.vk.com/access_token?client_id= + CLIENT_ID + &client_secret= + CLIENT_SECRET + &v=5.130&grant_type=client_credentials
#------------------------------------------

#{'link': 'http://example.com/some-page.html'}
#,'text':'hello world'}"
#'message': 'message text',
    
#vk_response    = self.req.wallPost(
#    vk_post.get('text'),
#	compiled_attachments,
#	into_group=into_group
#)

#print(vk_response.text)
#------------------------------------------

#vk_params = {
#    'group_id': '-' + vk_group_id,
#    'link': vk_api_url,
#    'text': 'text',
#    'v': vk_api_version,
#    'access_token': vk_token2,
#}

#vk_response   = requests.get(vk_url, params=vk_params)
#print(vk_response.text)

#------------------------------------------

#vk_url         = vk_api_url + "wall.post"
#vk_message     = "<b>Жирный текст</b>"

#vk_params = {
#    'v': vk_api_version,
#    'access_token': vk_token2,
#    'owner_id': '-' + vk_group_id, 
#    'from_group': '1', 
#    'message': 'hello',
#    'attachments': vk_api_url
#}

#vk_response   = requests.get(vk_url, params=vk_params)
#print(vk_response.text)

#------------------------------------------

#vk_params      = {
#                'owner_id': vk_group_id,
#                'from_group': vk_from_group,
#                'message': vk_message,
#                'v': vk_api_version,
#                'access_token': vk_token2
#                }

#vk_response   = requests.get(vk_url, params=vk_params)
#print(vk_response.text)

#------------------------------------------

#vk_content     = "message=" + vk_message
#vk_url         = "https://api.vk.com/method/wall.post?owner_id=-" + vk_group_id + "&from_group=1&scope=wall&" + vk_content + "&v=5.130&access_token=" + vk_token2
#vk_response    = requests.get(vk_url)
#print(vk_response.text)
