Insta_Share
=========

This project provides you with functions to be able to do the followings:
 *  Login into your instagram account and get the csrf_token and session_id by using login_instagram function
 *  Use the acquired credentials from output of the mentioned function to share a post into your Instagram account  
 *  Use the acquired credentials to upload a story
 
 # Installation #
 
```bash
    pip install requests
    pip install jsonlib
    pip install https://github.com/softcoder24/insta_share/archive/master.zip
```
 
 ## Usage ##
 
```python
from insta_share import Instagram

insta = Instagram()

session = {
    "csrf_token": "CSRF_TOKEN",
    "session_id": "SESSION_ID"
}

insta.load(session)

with open('toronto.jpg', 'rb') as image:
    share_post = insta.post(image, caption="Lovely City")
    print(share_post)
    
    story = insta.story(image)
    print(story)
    

```
Sample response for share_post: 
```
{'message': 'photo was shared successfully!', 
 'data': {'media': {'taken_at': 1605625037, 'pk': '2444482423770884550', 
    'id': '2444482423770884520_42370920440','device_timestamp': 1605625026, 
    'media_type': 1,
     ...
 'status': 'ok'}}

```
Sample response for story: 
```
{'message': 'story was shared successfully!', 
    'data': {'media': {'taken_at': 1605625634, 'pk': '2444487375272740605', 
    'id': '2444487375272740603_42370920439', 'device_timestamp': 1605625630,
    'media_type': 1, 
       ...
 'status': 'ok'}}

```