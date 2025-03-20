# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
Set（集合）: 无序且不允许重复元素，适用于 标签、去重等操作。
    SADD myset a b c    # 添加元素
    SREM myset a        # 删除元素
    SMEMBERS myset      # 获取所有元素
    SINTER set1 set2    # 求交集
    SRANDMEMBER key [count] #随机抽取值，不改变原集合
    SPOP key            # 随机弹出元素，改变原集合
"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.sadd('tags', 'python', 'redis', 'database')
print(r.smembers('tags'))  # {b'python', b'redis', b'database'}
