import requests


class ApiUser(object):
    def api_details(self, url, headers):
        url = url
        headers = headers
        requests.get(url=url,headers=headers)
        return requests.get(url=url,headers=headers)


