"""
进程间的通信通过队列（queue）来进行通信
    1.定义
        q=queue.Queue()
    2.使用
        q.put(1) 放值
        q.get() 取值
"""

from multiprocessing import Queue

# 定义队列中最多放多少数据
q = Queue(3)

# 使用put()方法放东西，如果队列满了，那继续put就只能等待前方的数据释放；否则就一直阻塞
q.put('a')
q.put('b')
q.put('c')

print("队列是否已满:",q.full()) # true
print("队列是否已空:",q.empty()) # false

# 判断一下队列是否满了，不满就放东西，满了就不放
if not q.full():
    # 如果3s之内没有放入，则不阻塞，结束put
    q.put('c',timeout=3)
else:
    print('队列已满')

# 获取队列的值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2)) # 在这一行时会报错，因为没有值可以取了

