# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
Hash（哈希）: 类似于 Python 的字典（key → {field1: value1, field2: value2}）。
    HSET user:1000 name Alice   # 设置哈希字段
    HGET user:1000 name         # 获取哈希字段
    HGETALL user:1000           # 获取所有哈希字段
    HDEL user:1000 age          # 删除某个哈希字段
    HKEYS key                   # 返回所有字段名
    HVALS key                   # 返回所有值
    HINCRBY key filed increment # 在字段对应值上进行整数增量运算
"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
print(r.hget('user:1000', 'name'))  # b'Alice'

r.hset('user:1000', 'name', 'Alice')
# 在redis 4.0+版本已被废弃
r.hmset("test",{"name":"alice","age":20})

# 一次添加多个字段，可以用hset
r.hset("test",mapping={"name":"alice","age":20})
