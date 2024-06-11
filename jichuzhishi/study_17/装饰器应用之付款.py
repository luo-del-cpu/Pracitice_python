#装饰器应用之付款功能
import time

islogin = False #默认是没有登录的

def log_in():
    username = input("请输入用户名：")
    passwd = input("请输入密码：")
    if username == 'admin' and passwd == '123':
        return True
    else:
        return False


#定义一个装饰器，进行付款验证
def login_required(func):
    def wrapped(*args,**kwargs):
        global islogin
        print('----正在付款----')
        if islogin:
            func(*args,**kwargs)
        else:
            print('用户未登录，请先登录！！！')
            islogin = log_in()
            #print(islogin)
    return wrapped


@login_required
def pay(money):
    print('正在进行付款，付款金额是{}'.format(money))
    time.sleep(2)
    print('付款成功！！！')

log_in()
pay(100)
pay(200)
