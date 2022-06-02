import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("received.json").read_json()
    arr = []
    for data in datas.values():
        arr.append((data.get("url"),
                    data.get("headers"),
                    data.get("data"),
                    data.get("status_code")))
    print(arr)
