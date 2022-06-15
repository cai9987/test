import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def read_json(self):
        with open(self.fileopen, 'r', encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("task.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("title"),
                     data.get("min_money"),
                     data.get("max_money"),
                     data.get("want_day"),
                     data.get("people_sum"),
                     data.get("describe"),
                     data.get("result")))
    print(arrs)
