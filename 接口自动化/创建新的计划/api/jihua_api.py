import requests


class JiHuaApi(object):
    def jihua_api(self,url,headers,data):
        url = url
        headers = headers
        data = data
        r = requests.post(url=url,headers=headers,json=data)
        return r


# if __name__ == '__main__':
#     JiHuaApi.jihua_api()
