# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
Sorted Set（有序集合）: 有序集合且不允许重复元素，适用排行榜操作。
    ZADD leaderboard 100 user1  # 添加元素
    ZINCRBY leaderboard 10 user1  # 增加分数
    ZRANK leaderboard user1  # 获取排名
    ZRANGE leaderboard 0 -1 WITHSCORES  # 获取排名列表
"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.zadd('leaderboard', {'Alice': 100, 'Bob': 200})
print(r.zrange('leaderboard', 0, -1, withscores=True))

