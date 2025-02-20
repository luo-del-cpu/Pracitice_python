"""
进程间的通信通过队列（queue）来进行通信
"""

from multiprocessing import Queue

q = Queue(3)

# 使用put()方法放东西
q.put('a')
q.put('b')
q.put('c')

# 判断一下队列是否满了，不满就放东西，满了就不放
if not q.qsize():
    q.put('c')
else:
    print('队列已满')