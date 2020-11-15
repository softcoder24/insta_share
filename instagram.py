import json
from datetime import datetime
import requests

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Credentials >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

insta_user = "YOUR USERNAME"
insta_password = "PASSWORD"


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Login into instagram account >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def login_instagram(username, password):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies['csrftoken']

    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:

        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf_token = cookie_jar['csrftoken']
        session_id = cookie_jar['sessionid']
        return csrf_token, session_id
    else:
        print("login failed ", login_response.text)


def share_photo(photo, caption=None):
    micro_time = int(datetime.now().timestamp())
    csrf_token, session_id = login_instagram(insta_user, insta_password)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< upload a photo into instagram server >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    headers = {
        "content-type": "image / jpg",
        "content-length": "1",
        "X-Entity-Name": f"fb_uploader_{micro_time}",
        "Offset": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/77.0.3865.120 Safari/537.36",
        "x-entity-length": "1",
        "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080,'
                                      f' "upload_media_width": 1080}}',
        "x-csrftoken": csrf_token,
        "x-ig-app-id": "1217981644879628",
        "cookie": "sessionid=" + session_id + "; csrftoken=" + csrf_token + ";"
    }

    upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                    data=open(photo, "rb"), headers=headers)

    json_data = json.loads(upload_response.text)
    upload_id = json_data['upload_id']

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< share a post from the uploaded photo >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if json_data["status"] == "ok":

        url = "https://www.instagram.com/create/configure/"

        payload = 'upload_id=' + upload_id + '&caption=' + caption +\
                  '&usertags=&custom_accessibility_caption=&retry_timeout='
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
            'x-instagram-ajax': 'adb961e446b7-hot',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.121 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/create/details/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
            'cookie': 'sessionid=' + session_id + '; csrftoken=' + csrf_token
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)

        if json_data["status"] == "ok":
            print("photo was shared successfully!")

    else:
        print(json_data)


share_photo(photo="toronto.jpg", caption="This is awesome")
