# 闭包的应用
'''
1.保存返回闭包时的状态（保存参数的状态）
2.计数器
3.同级访问
'''


# 1.闭包保存参数的状态
def func1(a, b):
    c = 10

    def inner_func1():
        s = a + b + c
        #print('s的值：', s)
        return s

    return inner_func1


x = func1(2, 3)  # 与下方的x_1两者互不影响
x_1 = func1(3, 4)

print("x_1():",x_1())  # --->得出17
print("x():",x())  # --->得出15


# 2.计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print('当期是第{}次访问'.format(container[0]))

    return add_one


counter = generate_count()
# 调用几次，记录一次状态
counter()
counter()
counter()


# 3.同级访问

def func2():
    a = 100

    def inner_func2():
        b = 10
        s = a + b
        print('s的值是：', s)

    def inner_func3():
        inner_func2()  # 可以对同级的变量进行访问,下方打印中a也是同理
        print('------>inner_func2',a)
        return 'hello'

    return inner_func3


x1 = func2()  # 此处因为返回值返回了inner_func3,所以需要一个变量去接，实际接的就是inner_func3()函数的地址；
              # 实际此处x1就代表了inner_func3（）函数
X2 = x1()  # 当调用x1(inner_func3())函数时，在内部函数中打开查看，有返回值”hello“,此时在外部调用时就需要使用一个变量去接；
print(X2) #得到的就是hello

'''
闭包的总结：

闭包的缺点：
1：作用域没有那么直观
2：因为变量不会被垃圾回收所以有一定的内存占用问题

闭包作用：
1.可以使用内部函数中同级的作用域
2.读取其他元素的内部变量
3.延长作用域

闭包总结：
1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.闭包的好处，使代码变得简洁，便于阅读代码
4.闭包是理解装饰器的基础
'''
