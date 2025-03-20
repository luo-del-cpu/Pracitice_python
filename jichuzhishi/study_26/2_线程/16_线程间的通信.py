# @Time : 2025/2/21 23:55
# @Author : luoxin

"""
线程间的通信：也可以说是生产者-消费者
    方式：使用queue队列通信，不同与进程的，是导入import queue
"""

import queue
import random
import threading
import time


def produce(q):
    i = 0
    while i<10:
        num = random.randint(1,100)
        # 将产生的数据放入队列
        q.put(f"生产者生成数据:{num}")
        print(f"生产者生成数据:{num}")
        time.sleep(0.5)
        i += 1
    q.put(None)


def consume(q):
    while True:
        # 从队列中拿数据
        item = q.get()
        if item is None:
            # 在结束前，告知队列已经完成任务，否则下方的q.join()会一直阻塞，主线程也无法得到释放
            q.task_done()
            break
        print("消费者拿到的数据:",item)
        time.sleep(1)
        # 完成任务，用于消费者通知队列已经完成任务
        q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)

    tp = threading.Thread(target=produce, args=(q,))
    tp.start()

    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    # 确保主线程阻塞，知道子线程完成
    tp.join()
    tc.join()

    # 等待队列中所有任务完成
    q.join()  # 必须调用 q.join() 来确保所有任务都完成

    print("END")