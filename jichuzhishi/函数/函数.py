import random

# #不带参数的函数
# def generate_random():
#     for i in range(10):
#         ran = random.randint(1, 20)
#         print(ran)
# print(generate_random)
#
# generate_random()

# 带参数的函数
'''
# 定义：
# def 函数（参数，参数。。。）
#     函数体
#
# 调用：
#     pass
'''


# 求随机数的函数，产生的个数未知
# def generate_name1(number):  # 形参：形式上的参数
#     for i in range(number):
#         ran1 = random.randint(1, 20)
#         print(ran1)
#
#
# print(generate_name1)
#
# # 调用
# generate_name1(5)  # 实参：实际的参数


#
# '''
# 定义一个登陆函数，参数是username，password
# 函数体：
# 判断参数传过来的username，password是否正确，如果正确则登陆成功，否则打印登陆失败
# '''
#
# def login(username, password):
#     uname = 'admin'
#     pwd = '123456'
#     for i in range(3):
#         if username == uname and password == pwd:
#             print("登陆成功")
#             break
#         else:
#             print("登陆失败")
#             username = input('输入你的用户名：')
#             password = input('输入你的密码：')
#     else:
#         print('账户锁定！')
#
#
# username = input('输入你的用户名：')
# password = input('输入你的密码：')
# login(username, password)
#
# '''
# 找出列表的最大值
# '''
#
#
def max(iterable):
    max = iterable[0]
    for i in iterable:
        if i > max:
            max = i
    print('最大值：', max)


# 调用 测试能否找出最大值
list1 = [3, 4, 1, 44, 344, 32, 3]
max(list1)

tuplel = (4, 53, 2, 1, 34, 55)
max(tuplel)


def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2, 3, 'h', d=6)
dict_1 = {'1': 'a'}


def aa(b, *a):
    '''
    :param b:
    :param a:
    :return:
    '''
    print(b, a)


aa(1, 2)
#
def bb(c, d):
    print('---文件夹的复制练习---')


print(id(bb(1, 2)))
print(id(bb(3, 4)))
print(id(None))
