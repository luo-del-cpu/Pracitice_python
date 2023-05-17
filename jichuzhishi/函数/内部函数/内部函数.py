# 内部函数：声明在函数内部的函数
'''
特点：
1.可以访问‘外部函数’的变量
2.内部函数可以修改外部函数的可变类型的值（例如：list等）
3.内部函数修改‘全局变量’的不可变变量时，需要在‘内部函数’中声明global 变量名
  内部函数修改外部函数的不可变的变量时，需要在‘内部函数’中声明nonlocal 变量名
4.locals()查看本地变量有哪些，以字典的形式输出
  globals()查看全局变量有哪些，以字典的形式输出，（注意里面会有一些系统的键值对）
'''

a = 100
print(globals())  # 查看全局的变量有哪些


def func():
    n = 100
    list1 = [1, 2, 3, 4, 5]  # 局部变量

    def inner_func():  # 声明内部函数
        nonlocal n  # 内部函数中修改外部函数中的局部变量（不可变的）需要加此声明
        global a  # 内部函数中修改全局变量的不可变变量时，需要加此声明
        for index, i in enumerate(list1):
            list1[index] = i + 5

        list1.sort()
        # 修改局部变量n的值
        n += 101
        # 修改全局变量a的值
        a += 100

    inner_func()  # 调用内部函数
    #print(locals())  # 使用locals()内置函数进行查看。可以看到在当前函数中声明的内容有哪些
                     # locals（）是以一个字典。key:value
    print('打印n的值：', n)
    print('打印list1中的值：', list1)
    print('打印a的值：', a)


func()
