import requests


class GetApi():
    def get_api(self):
        url = "http://test.zaitakugeek.cn:8000/hire/info"
        headers = {"Content-Type": "application/json",
                   "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"}
        params = {"demand_id": "111665393725670432"}

        r = requests.get(url=url,headers=headers,params=params)
        print(r.json())


if __name__ == '__main__':
    GetApi.get_api(1)
