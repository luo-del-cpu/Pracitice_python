# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
redis事务：
    是一组一次性、顺序执行的命令。事务内的所有命令都会按照提交顺序执行，
    但 Redis 事务并不支持回滚，这与传统数据库事务（ACID）有所不同。

基本特性：
    事务中的命令是按顺序依次执行的，不会被其他命令插入。
    事务不支持回滚，如果某个命令执行失败，已执行的命令不会撤销。
    事务可以用于批量执行多个命令，但它不是原子操作，可能部分成功，部分失败。
    事务通过 MULTI 开始，通过 EXEC 提交，或 DISCARD 取消。

pipeline：
    是 Redis 提供的一种批量操作机制，允许客户端在 一次网络请求 中 发送多个命令，
    减少 网络往返（RTT，Round Trip Time），提高执行效率。
"""

import redis

# 设置连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 创建Pipeline，可以 批量发送多个命令，然后一次性执行它们。
p = r.pipeline()

p.set("name","tom")
p.set("age","18")
p.get("name")
p.get("age")

# 一次将所有命令发送给redis，并且返回
p.execute()

