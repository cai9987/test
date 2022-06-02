import requests


class Catalogue(object):
    def catalogue_api(self):
        url = "http://test.zaitakugeek.cn:8000/hire/modify"
        params = {"demand_id": "111665393725670432"}
        headers = {"Content-Type": "application/json",
                   "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"}
        data = {
            "name": "修改需求",
            "speciality": 19,
            "min_salary": 230,
            "max_salary": 460,
            "expiry": "2022-02-26",
            "deadline": "33 00",
            "description": "2",
            "demand_id": "111665393725670432"
        }
        r = requests.post(url=url, headers=headers, params=params, json=data)
        print(r.json())


if __name__ == '__main__':
    Catalogue.catalogue_api(1)
