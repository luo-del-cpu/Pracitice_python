# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
redis:
    定义：
        是一种 基于内存 的 键值（key-value）存储，通常用于高性能缓存、消息队列、实时数据存储等。
        它支持多种数据结构，并提供丰富的功能，如持久化、事务、发布订阅、Lua 脚本等。
    特点：
        基于内存，读写速度快（可以达到 100,000+ QPS）。
        支持持久化，可选择 RDB（快照）或 AOF（日志）。
        支持多种数据结构，如字符串（String）、哈希（Hash）、列表（List）、集合（Set）、有序集合（Sorted Set）。
        支持分布式，可搭建主从复制、集群模式。
        支持事务，但不具备传统数据库的 ACID 性质。
        支持发布订阅（Pub/Sub），可用于消息队列等应用。
    存储要求：
        以字节的形式存储，如果是python对象（列表，字典，元组），需要序列化为json
"""

"""
# 字符串类型：常用于 缓存、计数器
    SET key value               # 存储字符串
    GET key                     # 获取字符串
    strlen key                  # 获取key存储值的长度
    getrange key start stop     # 获取对应索引之间（包含索引）的内容
    mset k1 vlaue1 k2 vlaue2    # 批量添加
    mget k1 k2                  # 批量获取
    INCR key                    # 递增（适用于数值）
    incrby key 步长              # 将key对应的值增加指定步长（适用于数值）
    DECR key                    # 递减（适用于数值）
    decrby key 步长              # 将key对应的值减少指定步长（适用于数值）
    APPEND key value            # 追加字符串
    ttl key                     # 查看过期时间
"""
import redis

# 创建redis连接对象
r = redis.Redis(host='localhost', port=6379, db=0)

# 可加ex参数表示过期时间，只有字符串类型有这个参数
r.set('name', 'Alice',ex=30)
print(r.get('name'))  # b'Alice'

r.incr('counter')  # 递增
print(r.get('counter'))  # b'1'

# 批量添加需要使用字典
r.mset({"k1":"v1", "k2":"v2"})


"""
过期时间删除的实现：
    1：惰性删除
    2：定期删除
    3：最大淘汰
    
    惰性删除：在进行get key的时候，去查是否过期，如果有，就进行删除。
    定期删除：主动定期扫描过期字典中的数据，检查是否过期
    最大淘汰：如果配置中打开maxmemory，那么如果超过此值，就会进行淘汰（使用不同的机制）
"""


