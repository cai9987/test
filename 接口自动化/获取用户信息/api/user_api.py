import requests


class TestUser(object):
    def user_api(self,headers,params,url):
        headers = headers
        params = params
        url = url

        r = requests.get(headers=headers,url=url,params=params)
        return r


# if __name__ == '__main__':
#     TestUser().user_api()
