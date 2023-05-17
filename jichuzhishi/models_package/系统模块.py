'''
当你导入一个模块，Python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录
3.如果都找不到，Python会查看默认路径、UNIX,默认路径一般为/usr/local/lib/python
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
'''

'''
自定义模块
系统模块
    sys
    time
    datetime
'''
# import sys
# import time
# import datetime
#
# print(sys.path)  # 打印找模块的路径
# print(sys.version)  # 打印Python解释器版本
# t = time.time()  # 打印时间戳
# print(t)
# time.sleep(3)  # 等待3秒
#
# # 将时间戳转换为字符串
# s = time.ctime(t)
# print(s)
# # 将时间戳转换为元组
# s1 = time.localtime(t)
# print(s1)
#
# # 将元组转换为时间戳
# s2 = time.mktime(s1)
# print(s2)
#
# # 将元组的时间转换为字符串
# s3 = time.strftime('%Y-%m-%d %H:%M:%S')
# print(s3)  # 得出：2021-05-19 21:14:14
#
# # 将字符串转换为元组
# s4 = time.strptime('2021/05/19', '%Y/%m/%d')
# print(s4)
#
# '''
# time模块重点：
#     time()
#     sleep()
#     strftime('格式')
# '''
#
# '''
# datetime模块：
#     time    时间
#     date    日期
#     datetime    日期时间
#     timedelta   时间差
# '''
# print(datetime.time.hour)  # 对象
# print(datetime.date.today())  # 得出：2021-05-19
# now = datetime.datetime.now()
# print(now)  # 得出：2021-05-19 21:29:01.902828
# timedel = datetime.timedelta(hours=2)  # 得出：时间差2hours
# print(now - timedel)  # 得出：2021-05-19 19:29:01.902828

'''
random模块：
    
'''
import random

# ran = random.random()  # 0-1之间的随机小数
# print(ran)
#
# ran = random.randrange(1, 10, 2)  # 1-10 -->1,3,5,7,9
# print(ran)
#
# ran = random.randint(1, 10)  # 包含1和10
#
# list = ['a', 'b', 'c']
# ran = random.choice(list)  # 随机抽取一个

list1 = ['的', '地方', 'df']
ran = random.shuffle(list1)
print(list1)
