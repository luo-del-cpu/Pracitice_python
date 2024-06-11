'''
加入购物车
判断用户是否登录，如果登录，成功加入购物车，否则提示请登录后添加
成功 True  失败  False
def shoppingcart(goodsname)
    pass

def login(username,passwd)
    pass
'''
import random

islogin = False  # 用于判断用户是否登录变量  默认是没有登录的


def add_shoppingcart(goodsname):
    global islogin  # 在函数内部时改变全局变量时，必须使用global声明一下
    if islogin:
        if goodsname:
            # 登录的
            print('成功将{}加入到购物车中'.format(goodsname))
        else:
            print('没有选中任何商品')
    else:
        # 没有登录
        answer = input('用户没有登录！是否登录？（yes/no）')
        if answer == 'yes':
            username = input('输入用户名：')
            passwd = input('输入密码：')
            # 调用login判断用户名和密码是否正确
            islogin = login(username, passwd)  # 在一个函数中调用另外一个函数
            print("islogin：",islogin)
        else:
            print('用户名或者密码错误！')


def login(username, passwd):
    if username == 'lijiaqi' and passwd == '123456':
        print('登录成功！！！')
        return True
    else:
        print('用户名或密码错误！！！')
        return False


username = input('输入用户名：')
passwd = input('输入密码：')

islogin = login(username, passwd)
print("外面的islogin",islogin)
add_shoppingcart('香水')


add_shoppingcart('测试')


def aaa(n):
    s = '123'
    for i in range(n):
        ran = random.randint(0,len(s)-1)
        return  ran
