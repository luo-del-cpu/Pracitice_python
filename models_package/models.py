class Art():
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('名字：{} 作者：{}'.format(self.name,self.author))


class Tag():
    def __init__(self, name):
        self.name = name
