# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
List（列表）只能存储字符串: 可用于消息队列（FIFO、LIFO）; 左进右出（队列），右进左出（栈）。
    LPUSH queue task1  # 从左侧插入
    RPUSH queue task2  # 从右侧插入
    LPOP queue         # 从左侧弹出
    BLPOP key timeout  # 列表头部，阻塞弹出，列表为空时阻塞，timeout为0永远阻塞
    RPOP queue         # 从右侧弹出
    BRPOP key timeout  # 列表尾部，阻塞弹出，列表为空时阻塞
    LREM key count value # 删除指定元素，count>0,从头部删除与value相同的count数；
                            <0从尾部；等于0，全部搜索
    LRANGE queue 0 -1  # 获取所有元素
    LLEN key           # 获取长度
"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.lpush('tasks', 'task1')
r.rpush('tasks', 'task2')

print(r.lrange('tasks', 0, -1))  # [b'task1', b'task2']
