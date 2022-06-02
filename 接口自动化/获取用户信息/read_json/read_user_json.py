import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def read_uesr_json(self):
        with open(self.fileopen, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("use.json").read_uesr_json()
    arr = []
    for data in datas.values():
        arr.append((data.get("headers"),
                    data.get("params"),
                    data.get("url"),
                    data.get("status_code")))
    print(arr)
