"""
进程传参
"""
import os

from multiprocessing import Process
from time import sleep


def task1(s,name):
    while True:
        sleep(s)
        print('这是任务一',os.getpid(),"-----",os.getppid(),name)


def task2(s,name):
    while True:
        sleep(s)
        print('这是任务二',os.getpid(),"-----",os.getppid(),name)


if __name__ == '__main__':

    # 因为在函数中定义了需要传参，所以可以在创建进程的时候使用args=()给函数传递参数
    # args参数需要是一个可迭代的，如果函数有两个参数，那么args也需要传递两个参数，就可以将2个参数分别传递给函数使用
    p = Process(target=task1, name='任务一',args=(1,'aa'))
    p.start()

    p1 = Process(target=task2, name='任务二',args=(2,'bb'))
    p1.start()

    # 阻塞主进程，等待子进程结束
    p.join()
    p1.join()
