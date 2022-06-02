# 调度功能函数，总控中心
import card_tool


# 循环菜单
#
def main():
    card_tool.load_file_data()
    while True:
        card_tool.show_menu()

        # 获取用户选择
        op = input("请输入你的选择")

        if op in ['1', '2', '3']:
            print("用户的操作.%s" % op)
            # 进一步判断
            if op == '1':
                print("你的选择是新建名片，请输入以下信息")
                card_tool.new_card()
            elif op == '2':
                card_tool.show_all()
            else:
                print("查询名片")
                card_tool.find_card()
        elif op == '0':
            # 保存内容到文件
            print("退出系统")
            card_tool.save_card()
            break
        else:
            print("输入错误，请重新输入")

    print("已退出该系统")


main()
