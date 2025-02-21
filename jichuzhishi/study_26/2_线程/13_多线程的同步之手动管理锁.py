# @Time : 2025/2/21 21:19
# @Author : luoxin
# @Time : 2025/2/21 19:28
# @Author : luoxin

"""
多线程修改同一个变量:
    加锁方式：
        1：先创建锁：lock = threading.Lock()
        2：手动创建或自动管理
            手动创建：
                lock.acquire()
                临界区代码
                lock.release()
            自动管理：with lock：
                        临界区代码
"""

import threading

money = 0
lock = threading.Lock()

def task1():
    global money
    lock.acquire() # 申请锁，阻塞
    for _ in range(1000000):
        money += 1
    print("task1-money",money)
    lock.release() # 释放锁

def task2():
    global money
    lock.acquire()
    for _ in range(1000000):
        money += 1
    print("task2--money",money)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1,name='task1')
    t2 = threading.Thread(target=task2,name='task2')


    t1.start()
    t2.start()


    t1.join()
    t2.join()


    print(f"money剩余:{money}")