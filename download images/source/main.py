import os

from vk.users import *
from vk.photos import *

vk_token        = "ea01d0aca61981ecfcdee53e592e881bf1a6d621b604cc9db1edff3c6828634c7e4f4022eebed197f9c6a"
vk_user_id      = "522142542"

vk_user_info    = vk_get_user_info(vk_token, vk_user_id)
print(vk_user_info)

vk_photo_albums = vk_get_photo_albums(vk_token, vk_user_id)
vk_album_title  = "test"
vk_album_id     = "269851398"
vk_find_album   = vk_find_photo_album(vk_album_title, vk_photo_albums)
print(vk_photo_albums)

filepath        = "./data/test1.jpg"
if vk_find_album == False:
    response = vk_create_photo_album(vk_token, vk_album_title, vk_album_title)
    print("vk_create_photo_album:", response)
else:
    if os.path.exists(filepath) == True:
        response = vk_upload_photo(vk_token, vk_user_id, vk_album_id, filepath)
        print("vk_upload_photo:", response)

