# 继承之has a
'''
知识点：
1.has a
    一个类中使用了另外一种自定义的类型
2.类型
    系统类型：
        str list...
    自定义类型:
        算是自定义的类，都可以将其当成一种类型
        s = Student
        s是Student类型的一个对象
'''


class Computer():
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def run(self):
        print('使用电脑上网！')

    def __str__(self):
        return '电脑品牌：{} 型号：{} 颜色：{}'.format(self.brand, self.type, self.color)


class Book():
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def read(self):
        print('获取知识！')

    def __str__(self):
        return '书名：{} 作者：{} 数量：{}'.format(self.bname, self.author, self.number)


class Student():
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            # 判断传入的书籍名是否与书箱【self.books】里的书名重复，重复就代表借过
            if book1.bname == book.bname:
                print('已经借过了！')
                break
        else:
            # 将对象参数book添加到列表中
            self.books.append(book)
            print('添加成功')

    def show_book(self):
        for book in self.books:  #
            """因为在self.books的列表在添加的时候，传入的就是book对象，
            所以，这里遍历出来的每一个book就是一个book对象"""
            print(book.bname)  # 此处只需要打印出书的名字，通过book对象查看name

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


# 创建对象
# 先创建子类的对象；因为父类中会用到子类里的属性，先有了子类里的属性，父类才能用
computer = Computer('联想', 'A186', '白色')
book = Book('盗墓笔记', '南派三叔', '10')
# print(book)
stu = Student('张三', computer, book)
# print(stu)

# 先看一下学生借了哪些书
stu.show_book()
# 定义一本书，鬼吹灯
books1 = Book('鬼吹灯', 'aaa', '8')
# print(books1)

print('-------------------------')
stu.borrow_book(books1)
stu.show_book()
