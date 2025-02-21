"""
加锁方式：
    自动管理：with lock：
                临界区代码
"""
import threading

money = 0
lock = threading.Lock()  # 创建一个锁

def task1():
    global money
    with lock:  # 使用锁来确保线程安全
        for _ in range(1000000):
                money += 1
    print("task1-money:", money)

def task2():
    global money
    with lock:
        for _ in range(1000000):
                money += 1
    print("task2-money:", money)

if __name__ == '__main__':
    t1 = threading.Thread(target=task1, name='task1')
    t2 = threading.Thread(target=task2, name='task2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"money剩余: {money}")
