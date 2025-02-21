"""
进程池:
    1.概念
        当需要的进程数量不多时，可是使用Process动态生成进程。但是，当需要成百上千个进程时，可以使用multiprocessing模块的Pool方法；
        初始化Pool时，可以指定一个最大进程数，当有新地请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程来执行该请求；
        如果满了，那么该请求就会暂停，知道池中有进程结束，才会创建新的进程来执行。
    2.两种不同的方式
        阻塞式：添加一个执行一个任务，如果一个任务不结束，另一个任务就进不来
        非阻塞式：全部添加到队列中，立刻返回(指的是将一个进程放入进程池之后继续放入)，并没有等待其它进程执行完毕。
        回调函数是等待任务完成之后才调用
    3.格式
    pool = Pool(3)
    pool.apply_async()/pool.apply()
    pool.close() 添加任务结束
    pool.join() 主进程让步，等待子进程结束
"""
import os
from multiprocessing import Pool
import time

# 非阻塞式进程
from random import random


def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    return '完成任务:{};用时：{};进程id：{}'.format(task_name,(end - start),os.getpid())


# 使用回调函数来接收task执行完成之后返回的值
container = []
def callback(n):
    container.append(n)

if __name__ == '__main__':
    pool = Pool(5)

    # 有6个任务，大于池子的5
    tasks = ['听音乐', '洗衣服', '跑步', '做饭', '学习', '上班']
    for task1 in tasks:
        # 非阻塞式：apply_async(任务，参数，回调函数...)
        pool.apply_async(task, args=(task1,),callback=callback)

    pool.close()  # 添加任务结束

    pool.join()  # 让主进程让步，意思就是不让主进程做事，这样主进程会一直活着，子进程也可以一直活着

    # 确保所有任务完成之后，在进行调用，否则可能会导致任务还没有完成，无法往container添加内容
    for i in container:
        print(i)

    print('over')


