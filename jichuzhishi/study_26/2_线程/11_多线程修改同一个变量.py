# @Time : 2025/2/21 19:28
# @Author : luoxin

"""
多线程修改同一个变量:如果在数据量比较大的情况下，是会有问题的
    原因：具体原因看"12_对11补充"的文件
"""

import threading

money = 0


def task1():
    global money
    for _ in range(1000000):
        money += 1
    print("task1-money",money)

def task2():
    global money
    for _ in range(1000000):
        money += 1
    print("task2--money",money)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1,name='task1')
    t2 = threading.Thread(target=task2,name='task2')


    t1.start()
    t2.start()


    t1.join()
    t2.join()


    print(f"money剩余:{money}") # 得出的数字可能小于2000000