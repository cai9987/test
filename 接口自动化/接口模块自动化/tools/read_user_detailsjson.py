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
    datas = ReadJson("user_details.json").read_json()
    # 新建空列表，读取json数据
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("headers"),
                     data.get("status_code")))

    print(arrs)