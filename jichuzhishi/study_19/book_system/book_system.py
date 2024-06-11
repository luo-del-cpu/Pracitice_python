# @Time : 2024/6/4 21:59
# @Author : luoxin

"""
模拟一个图书管理系统
持久化保存使用文件
"""

# 用户注册
def register():
    username = input("输入用户名：")
    passwd = input("输入密码：")
    repasswd = input("确认密码：")

    if passwd == repasswd:
        #保存信息
        with open(r"./user.txt",'a') as w:
            w.write(f'{username} {passwd}\n')
        print("用户注册成功")
    else:
        print("两次密码不一致！！！")

# 用户登录
def login():
    username = input("输入用户名：")
    passwd = input("输入密码：")

    if username and passwd:
        with open('./user.txt','r') as rstream:
            while True:
                user = rstream.readline()
                if not user:
                    print("用户名或密码输入错误！！！")
                    break
                input_user = f'{username} {passwd}\n'
                if user == input_user:
                    print("用户登录成功！！！")
                    break

def show_book():
    print("---书名如下---")
    with open('./books.txt','r') as f:
        books = f.readlines()
        for book in books:
            print(book,end='')

#register()
#login()
show_book()