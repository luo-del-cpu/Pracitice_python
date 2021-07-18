class User():
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def login(self, username, passwd):
        if username == self.username and passwd == self.passwd:
            print('登录成功')
        else:
            print('登录失败')

    def show(self):
        print(self.username, self.passwd)

    def publish(self, art):
        print(self.username, '发表了文章：', art.name)
