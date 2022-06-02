# 功能函数的实现和定义
# 实现功能：显示菜单  新建名片 显示全部名片 查询名片 修改名片 删除名片 退出系统
# 定义一个全局参数
import os
card_list = []#{"name": "李白", "age": '22', "sex": "男", "mail": "1234@qq.com"},
#              {"name": "貂蝉", "age": '21', "sex": "女", "mail": "1555@qq.com"},
#              {"name": "孙策", "age": '34', "sex": "男", "mail": "166@qq.com"},
#              {"name": "李信", "age": '25', "sex": "男", "mail": "1624@qq.com"},
#              {"name": "魏征", "age": '67', "sex": "男", "mail": "1784@qq.com"}


# 定义菜单函数
def show_menu():
    """
    显示菜单函数
    :return:
    """
    print("")
    print("")
    print("*" * 50)
    print("欢迎使用[名片管理系统] v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新建名片"""
    # 获取信息
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    sex = input("请输入你的性别：")
    mail = input("请输入你的邮箱：")
    # 创建一个列表保存信息
    new_dict = {
        'name': name,
        'age': age,
        'sex': sex,
        'mail': mail
    }
    # 添加到全局列表
    card_list.append(new_dict)

    print("%s新建成功" % name)


def show_all():
    """
    显示全部名片
    :return:
    """
    # 为空时，不显示信息
    if len(card_list) <= 0:
        print("当前列表没有名片信息")
        return
    print("显示全部名片")
    print("-" * 50)
    print("姓名".ljust(5), "年龄".ljust(5), "性别".ljust(5), "邮箱".ljust(5), sep="\t\t")
    print("-" * 50)
    # 不为空时，显示所有信息
    for item in card_list:
        # 获取列表中的字典
        print(item.get('name').ljust(5), item.get('age').ljust(5), item.get('sex').ljust(5),
              item.get('mail').ljust(5), sep="\t\t")


def find_card():
    """
    查询名片
    :return:
    """
    # 输入查找的信息
    find_dict = input("请输入名片信息,如名字，年龄，邮箱，输入0退出查询名片：")
    for i in card_list:
        # 用名字查询
        if i.get('name') == find_dict:
            print("-" * 50)
            print("姓名".ljust(5), "年龄".ljust(5), "性别".ljust(5), "邮箱".ljust(5), sep="\t\t")
            print("-" * 50)
            print(i.get('name').ljust(5), i.get('age').ljust(5), i.get('sex').ljust(5),
                  i.get('mail').ljust(5), sep="\t\t")
            print("-" * 50)
            deal_card(i)  # 调用函数，显示修改列表，i为查询到的字典
            break
        # 用年龄查询
        elif i.get("age") == find_dict:
            print("-" * 50)
            print("姓名".ljust(5), "年龄".ljust(5), "性别".ljust(5), "邮箱".ljust(5), sep="\t\t")
            print("-" * 50)
            print(i.get('name').ljust(5), i.get('age').ljust(5), i.get('sex').ljust(5),
                  i.get('mail').ljust(5), sep="\t\t")
            print("-" * 50)
            deal_card(i)  # 调用函数，显示修改列表，i为查询到的字典
            break
        # elif i.get("sex") == find:
        #     print("-" * 50)
        #     print("姓名".ljust(5), "年龄".ljust(5), "性别".ljust(5), "邮箱".ljust(5), sep="\t\t")
        #     print("-" * 50)
        # for item in card_list:
        #     # 获取列表中的字典
        #     print(item.get('name').ljust(5), item.get('age').ljust(5), item.get('sex').ljust(5),
        #           item.get('mail').ljust(5), sep="\t\t")
        # print(i.get('name').ljust(5), i.get('age').ljust(5), i.get('sex').ljust(5),
        #       i.get('mail').ljust(5), sep="\t\t")
        # break
        # 用邮箱查询
        elif i.get("mail") == find_dict:
            print("-" * 50)
            print("姓名".ljust(5), "年龄".ljust(5), "性别".ljust(5), "邮箱".ljust(5), sep="\t\t")
            print("-" * 50)
            print(i.get('name').ljust(5), i.get('age').ljust(5), i.get('sex').ljust(5),
                  i.get('mail').ljust(5), sep="\t\t")
            print("-" * 50)
            deal_card(i)  # 调用函数，显示修改列表，i为查询到的字典
            break
        elif find_dict == "0":
            print("已退出查询名片")
            break
    # 没有是返回错误
    else:
        print("你的输入有误")


# 名片操作选择
def deal_card(find):  # find是形参
    """
    对名片进行修改删除
    :return:
    """
    tel = input("请输入对名片的操作选择:[1、修改][2、删除][0、返回上一级]：")
    if tel == "1":
        print("你的请求是修改")
        # find里面的内容是 i 字典内容     find.get('name')为input_card_info（）函数的实参
        find['name'] = input_card_info(find.get('name'), "请输入姓名")
        find['age'] = input_card_info(find.get('age'), "请输入年龄")
        find['sex'] = input_card_info(find.get('sex'), "请输入性别")
        find['mail'] = input_card_info(find.get('mail'), "请输入邮箱")
        return

    elif tel == "2":
        print("你的请求是删除")
        card_list.remove(find)
        print("信息已经被删除")
    elif tel == "0":
        print("返回上一级")
        return
    else:
        print("你的输入错误")


def input_card_info(dict_value, msg):
    # 使用input（）函数获取用户信息
    info = input(msg)
    # 判断用户信息是否为空
    if len(info) > 0:
        return info
    else:
        return dict_value


# 把名片列表保存在文件中
def save_card():
    # 打开文件
    file = open("card_data.txt", "w",encoding="utf-8")
    file.write(str(card_list))
    file.close()

# 当下次启动时，要打开文件，读取文件内容到列表中
def load_file_data():
    """
    当前函数当下次启动时，要打开文件，读取文件内容到列表中
    :return:
    """
    # 判断card_data.txt 是否存在
    if os.path.exists("card_data.txt"):
        # 打开card_data文件
         file = open("card_data.txt" , "r" , encoding = "utf-8")
        # 将read信息写入file
         text = file.read()

        # 转换成字典
         if len(text) == 0:
             print("文件为空")
             file.close()
             return
         else:
             # 修改全局变量
            global card_list
            card_list = eval(text)# eval不能实现为空转换
         file.close()
    else:
         print("保存列表不存在")

