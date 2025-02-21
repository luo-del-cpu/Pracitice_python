# @Time : 2025/2/21 23:24
# @Author : luoxin

"""
死锁：
    资源使用不当，导致无法进行下去；比如说A锁拥有B锁，B锁又拥有A锁
解决：
    1:重构代码
    2:使用timeout
"""
import threading
import time

LockA = threading.Lock()
LockB = threading.Lock()

# 也可以定义自己的线程，继承Thread就行
class MyThread(threading.Thread):
    def run(self):
        if LockA.acquire():
            print(self.name+"获取了A锁")
            time.sleep(0.5)
            if LockB.acquire(timeout=3):
                print(self.name+"又获取了B锁，我还有个A锁")
                LockB.release()
            LockA.release()

class MyThread1(threading.Thread):
    def run(self):
        if LockB.acquire():
            print(self.name+"获取了B锁")
            time.sleep(0.5)
            if LockA.acquire(timeout=3):
                print(self.name+"又获取了A锁，我还有个B锁")
                LockB.release()
            LockA.release()

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()