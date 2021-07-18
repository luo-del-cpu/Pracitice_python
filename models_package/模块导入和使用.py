'''
在Python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件（.py）就是一个模块（moudle）,
模块名就是文件名去掉后缀py,这样做的好处是：

-提高代码的可复用性、可维护性。一个模块编写完成后，可以很方便的在其他项目中导入
-解决了命名冲突，不同模块中相同的命名不会冲突

常用标准库：见B站视频模块导入和使用

1.自定义模块
2.使用一些系统模块

导入模块：
1.import 模块名
    模块名.函数(类、变量)
2.from 模块名 import 变量名|函数|类
3.from 模块名 import*
    导入该模块中所有的内容
    但是如果想限制获取的内容，可以在模块中使用__all__=[使用*可以访问到的内容]
4.无论是import还是from的形式，都会将模块内容进行加载
    如果不希望其进行调用。就会用到__name__
具体注意事项可看B站收藏中的千峰宋宋老师的模块导入内容
'''
list1 = [4, 3, 4, 5]
# 需要计算list1中的和，就需要叫caculate里面的函数来帮忙
# import caculate  # 导入模块
#
# # 使用模块中的函数
# result = caculate.add(*list1)  # 此处注意，要想使用函数就得用“模块名.函数（类、变量等）”来调用
# print(result)
#
# # 使用函数的变量
# print(caculate.number)  # 得出：100
#
# # 使用模块当中的类
# c = caculate.Caculate(8)
# c.show()  # 得出：caculate中的类
#
# # 使用模块中的类方法
# caculate.Caculate.test1()  # 得出：caculate中的类方法

# from caculate import add,number,Caculate  # 只导入模块中的一部分,导入多个加“，”分隔即可
#
# print(add(*list1),number)
#
# c = Caculate(80)
# c.show()

from caculate import *
test2()
