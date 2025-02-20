"""
1.概念：
    进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，
是操作系统结构的基础。在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向线程设计的计算机结构中，
进程是线程的容器。程序是指令、数据及其组织形式的描述，进程是程序的实体。

2.优点：
    稳定性高，一个进程崩溃了，不会影响其他进程；
3.缺点：
    创建进程开销巨大；
    操作系统能同时运行进程数目有限；

from multiprocessing import Process--->windows系统下创建进程需先导入模块

process = Process(target=函数，name=进程的名字，args=(给函数传递的参数))
process 对象

对象调用方法：
process.start()--->启动进程并执行任务
process.run()--->只是启动了任务并没有启动进程
process.terminate()--->终止进程

目的：
可以同时快速的进行多任务，此处的同时是一个伪“同时”，只是cpu在轮巡进行调度执行
"""

# 进程创建
from multiprocessing import Process
from time import sleep


def task1():
    while True:
        sleep(1)
        print('这是任务一')


def task2():
    while True:
        sleep(1)
        print('这是任务二')


if __name__ == '__main__':
    # 子进程
    # target=函数 name=进程的名字 args=给函数传递参数
    p = Process(target=task1, name='任务一')
    # start()启动进程并且执行任务；run()只是执行动作，没有启动进程
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务二')
    p1.start()
    print(p1.name)

    # 终止进程
    p.terminate()