import requests
import json


url_api = 'https://apieasycall.ptl.ru/api/ver1.0'


def create_token():
    url_for_token = 'https://apieasycall.ptl.ru/oauth/token'
    params = {
        "Content-Type" : "application/x-www-form-urlencoded",
        'grant_type' : 'client_credentials',
        'client_id': '612b052661a049328ebe4411d6b6da96',
        'client_secret': '9f322177697347b484595de76d4e95c5'
    }
    token_get = requests.post(url_for_token, params=params)
    token = json.loads(token_get.text)['access_token']
    print(f'Токен: {token} - ПОЛУЧЕН!')
    return token

def get_info(token):
    client_id = 1795
    users = {}
    url_z = f'{url_api}/client/@me/extension/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url_z, headers=headers)
    for p in json.loads(response.text):
        users[p["name"]] = p["id"]
        print(f'name:{p["name"]}--caller_id_name:{p["caller_id_name"]}--type:{p["type"]}--id:{p["id"]}')
    print(users)
    return users





def callback(src_num,dst_num,ext_id,token):
    url_z = f'{url_api}/extension/@{str(ext_id)}/callback/'
    headers ={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        "caller_id_name": str(dst_num),
        "dst_num": str(dst_num),
        "src_num": [f'{str(src_num)}']
    }
    response = requests.post(url_z, headers=headers, data=json.dumps(data))
    print(url_z)
    print(data)
    print(response.text)
    return

token = create_token()
users_id = get_info(token)
src_num = 100
dst_num = 500833
ext_id = src_num
print(ext_id)
callback(src_num,dst_num,ext_id,token)
