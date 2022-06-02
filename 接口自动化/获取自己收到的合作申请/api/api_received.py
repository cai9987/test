

import requests


class ApiReceived(object):
    def api_received_work(self,url,headers,params):
        url = url
        headers = headers
        params = params

        r = requests.get(url=url, headers=headers, params=params)
        print(r.json())
        return r


if __name__ == '__main__':
    ApiReceived.api_received_work(1)
