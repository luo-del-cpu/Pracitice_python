'''
图书管理系统:
1.持久化保存：文件
    list，元组，字典都不是持久化保存

'''


# 定义一个用户注册的函数
def register():
    username = input('输入用户名：')
    passwd = input('输入密码：')
    repasswd = input('输入确认密码：')

    if passwd == repasswd:
        # 保存信息,不能使用'w'mode模式，否则每次添加会清空之前的信息
        with open(r'C:\Users\86176\Desktop\python\book\users.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, passwd))
        print('用户注册成功')
    else:
        print('密码不一致！！！')


# 定义一个用户登录函数
def login():
    username = input('输入用户名：')
    passwd = input('输入密码：')
    if username and passwd:
        with open(r'C:\Users\86176\Desktop\python\book\book.txt') as wstream:
            while True:
                user = wstream.readline()

                if not user:
                    print('用户名或者密码有误！')
                    break
                input_user = '{} {}\n', format(username, passwd)
                if user == input_user:
                    print('用户登录成功！')
                    break


# 定义一个打开书籍的文件
def show_books():
    print('------图书馆里的书籍------')
    with open(r'C:\Users\86176\Desktop\python\book\book.txt', 'r', encoding='utf-8') as rstream:
        books = rstream.readlines()
        for i in books:
            print(i, end='')


# 调用函数，相当于注册用户
register()
# 调用函数，用户登录
login()
# 调用函数，查看有什么书籍
show_books()
