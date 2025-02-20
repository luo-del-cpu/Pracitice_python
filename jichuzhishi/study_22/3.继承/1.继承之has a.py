"""
继承之has a
1.定义
    一个类中使用了另外一种自定义的类型，例如下方81行中的stu对象使用了computer和book对象
2.类型
    系统类型：
        str list...
    自定义类型:
        算是自定义的类，都可以将其当成一种类型
        s = Student
        s是Studet()t类型的一个对象
"""


# 定义电脑的类，有品牌，型号，颜色的属性
class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def run(self):
        print('使用电脑上网！')

    def __str__(self):
        return '电脑品牌：{} 型号：{} 颜色：{}'.format(self.brand, self.type, self.color)


# 定义书的类，有书名，作者，数量属性
class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def read(self):
        print('获取知识！')

    def __str__(self):
        return '书名：{} 作者：{} 数量：{}'.format(self.bname, self.author, self.number)


# 定义学生类，有名字，电脑，书的属性
class Student:
    def __init__(self, name, own_computer, own_book):
        self.name = name
        self.computer = own_computer
        # 初始化一个存储书籍的空列表
        self.books_list = []
        self.books_list.append(own_book)

    # 此处的new_book实际就要传入一个book的对象
    def borrow_book(self, new_book):
        for b_book in self.books_list:
            # 判断传入的书籍名是否与书箱【self.books_list】里的书名重复，重复就代表借过
            if b_book.bname == new_book.bname:
                print(f'{new_book.bname}已经借过了！')
                break
        else:
            # 将对象参数book添加到列表中
            self.books_list.append(new_book)
            print(f'{new_book.bname}已添加到我的书库')

    def show_book(self):
        """
        :return: 拥有的书籍名称
        """
        # 因为在self.books_list的列表在添加的时候，传入的就是book对象，所以，这里遍历出来的每一个book就是一个book对象
        book_names = ",".join([show_book.bname for show_book in self.books_list ])
        print(f"我现在拥有的书籍:{book_names}")

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books_list)


# 先创建子类的对象；因为父类中会用到子类里的属性，先有了子类里的属性，父类才能用
computer = Computer('联想', 'A186', '白色')
book = Book('盗墓笔记', '南派三叔', '10')
# 此处 将computer与book对象 给Student()实例化时 用作参数
stu = Student('张三', computer, book)



print('----------第一次查看学生拥有的书籍---------------')
stu.show_book()
# 重新定义一本书：鬼吹灯
book1 = Book('鬼吹灯', 'aaa', '8')

print('----------进行借书操作---------------')
stu.borrow_book(book1)
print('----------再次查看学生拥有的书籍---------------')
stu.show_book()
