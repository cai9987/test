import requests


class DemandApi(object):
    def demand_api(self, url, headers, params):
        url = url
        headers = headers

        params = params

        r = requests.get(url=url, headers=headers, params=params)
        return r


# if __name__ == '__main__':
#     DemandApi.demand_api()
