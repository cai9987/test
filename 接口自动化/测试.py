import requests


def phone_login():
    url = "http://test.zaitakugeek.cn:8000/user/phone_login"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "verify_code": "595342",
        "phone": "15018248542",
        "region_code": "86"
    }
    r = requests.post(url=url, json=data, headers=headers)
    print(r.json())
    print(r.status_code)


r = requests.get('https://b.faloo.com/1119556_66.html')

print(type(r))

print(r.encoding)

print(r.apparent_encoding)

print((r.text.encode(r.encoding).decode(r.apparent_encoding)))
