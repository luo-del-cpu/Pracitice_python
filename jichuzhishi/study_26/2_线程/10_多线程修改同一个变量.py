# @Time : 2025/2/21 19:28
# @Author : luoxin

"""
多线程修改同一个变量:如果在数据量比较小的情况下，是没有问题的
"""
import threading

money = 1000


def task1():
    global money
    for _ in range(100):
        money -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=task1,name='task1')
    t2 = threading.Thread(target=task1,name='task2')
    t3 = threading.Thread(target=task1,name='task3')
    t4 = threading.Thread(target=task1,name='task4')

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(f"money剩余:{money}") # 得出600