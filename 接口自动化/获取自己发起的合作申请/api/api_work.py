import requests


class ApiWork(object):
    def api_work(self,url,headers):
        url = url
        headers = headers

        r = requests.get(url=url, headers=headers)
        return r





