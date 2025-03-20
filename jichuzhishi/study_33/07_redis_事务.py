# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
pipeline与事务结合
    with r.pipeline(transaction=True) as p:
        transaction=True：开启事务，不需要手动调用p.multi()。
        transaction=False：不开启事务，如果手动调用p.multi()会报错。
"""

import redis

# 设置连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 创建Pipeline，transaction打开事务，可以忽略写p.multi()。
with r.pipeline(transaction=True) as p:
    p.set("name","tom")
    p.set("age","18")
    p.get("name")
    p.get("age")

# 一次将所有命令发送给redis，并且返回
p.execute()

