"""
1：使用input()方法必须使用一个变量来接收输入流中的信息
2：input方法是阻塞式的，必须通过键盘输入一个信息，敲击回车，来在控制台中打印出需要的信息
3：input键盘输入的都是字符串类型，即使输入的是500这样整数类型的数字
"""
a=1
print('测试：'+a)
# print("""
# *************
# 捕鱼达人
# *************
# """)
#
# name = input("请输入账号：")
# password = input("请输入密码：")
# print(f'账号：{name}')
# print(f'密码：{password}')
# money = input("请输入充值金额：")
# print(f'您已充值{money}元')

# name = input("输入你的名字：")
# age = input("输入你的年龄：")
# height = input("输入你的身高：")
# msg = '''
# -----------info---------
# Name   : %s
# Age    : %s
# height : %s
# -----------end-----------
# '''%(name,age,height)
# print(msg)
# print(name,age,height)
#
# name = input("输入你的名字：")
# age = input("输入你的年龄：")
# height = input("输入你的身高：")
# msg = f'''
# -----------info---------
# Name   : {name}
# Age    : {age}
# height : {height}
# -----------end-----------
# '''
# print(msg)
#
# gong_zi = int(input("你的工资: \n"))
# if gong_zi < 1000 :
#     print("老板，我是你爹")
# elif gong_zi < 2000 :
#     print("老板，你还是有病")
# elif gong_zi < 5000 :
#     print("老板脑子有坑，背后说坏话")
# elif gong_zi < 10000 :
#     print("老板说的有点问题，但我不说话")
# else :
#     print("老板说啥是啥吧")
#
# print('''
# *****************
# 捕鱼达人
# *****************
# ''')
# name = input("请输入你的名字：")
# passwd = input("请输入密码：")
# print("%s充值才能进入游戏" %name)
# coins = int(input("请输入充值的金额："))
# print("%s充值成功，充值金额：%d"%(name,coins))
#
# print('''
# *****************
# 王者荣耀
# *****************
# ''')
# print("游戏：王者荣耀")
# character = input("请选择角色：")
# zhuang_bei = input("请选择装备：")
# buy_zhuangbei = input("请输入想购买的装备：")
# goumai = int(input("请输入购买的金额："))
# print("%s拥有%s、%s装备，花了%d元" %(character,zhuang_bei,buy_zhuangbei,goumai))
