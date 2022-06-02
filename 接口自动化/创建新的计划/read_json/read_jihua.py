import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def jihua(self):
        with open(self.fileopen, 'r', encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    data = ReadJson("jihua.json").jihua()
    arr = []
    for i in data.values():
        arr.append((i.get("url"),
                    i.get(""),
                    i.get("data")))
        print(i)
