import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_proposal(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    data = ReadJson("work.json").read_proposal()
    arr = []
    for i in data.values():
        arr.append((i.get("url"),
                    i.get("headers"),
                    i.get("status_code")))

    print(arr)
