import json


class ReadJson(object):
    # 对json文件路径进行包装
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        # 打开json文件
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    # ReadJson("login.json").read_json()
    data = ReadJson("login.json").read_json()
    # 新建空列表，读取json数据
    arrs = [(data.get("url"),
             data.get("account"),
             data.get("password"),
             data.get("status_code"))]
    print(arrs)
