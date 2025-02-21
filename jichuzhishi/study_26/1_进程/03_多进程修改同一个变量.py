"""
多进程同时修改一个变量：
    多进程对于全局变量的访问，在每一个进程内都会放一个全局变量m,list ，如下举例所示；保证每个进程不互相干扰
"""
import os

from multiprocessing import Process
from time import sleep

m = 1 # 不可变类型
list = [] # 可变类型

def task1(s):
    global m
    while True:
        sleep(s)
        m +=1
        list.append(str(m)+"task1")
        print('这是任务一',m,list)


def task2(s):
    global m
    while True:
        sleep(s)
        m += 1
        list.append(str(m)+"task2")
        print('这是任务二',m,list)


if __name__ == '__main__':


    p = Process(target=task1, name='任务一',args=(1,))
    p.start()

    p1 = Process(target=task2, name='任务二',args=(2,))
    p1.start()

    while True:
        sleep(1)
        m +=1
        list.append(str(m)+"task-main")
        print("--------main:",m)