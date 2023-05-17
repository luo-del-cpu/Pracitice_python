'''
阻塞式：添加一个执行一个任务，如果一个任务不结束，另一个任务就进不来
非阻塞式：全部添加到队列中，立刻返回，并没有等待其它进程执行完毕，但是回调函数时等待任务完成之后才调用
'''
import os
from multiprocessing import Pool
import time

# 非阻塞式
from random import random


def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务:{};用时：{};进程id：{}'.format(task_name,(end - start)),os.getpid())


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '洗衣服', '跑步', '做饭', '学习', '上班']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,))

    pool.close()  # 添加任务结束
    pool.join()  #

    print('over')


