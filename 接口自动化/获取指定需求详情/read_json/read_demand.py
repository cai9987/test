import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def read_proposal(self):
        with open(self.fileopen, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    data = ReadJson("demand.json").read_proposal()
    arr = []
    for i in data.values():
        arr.append((i.get("url"),
                    i.get("headers"),
                    i.get("params"),
                    i.get("status_code")))

    print(arr)

