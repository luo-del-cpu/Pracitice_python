# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
redis的主从复制+哨兵：高可用的解决方案
    在生产环境中，我们需要处理 Sentinel 连接异常，保证 Redis 高可用。
"""

import redis
from redis.sentinel import Sentinel
import time

# Sentinel 配置
sentinel_hosts = [
    ('192.168.1.200', 26379),
    ('192.168.1.201', 26379),
    ('192.168.1.202', 26379)
]

# 重试 Sentinel 连接
def connect_sentinel(retries=5, delay=2):
    for i in range(retries):
        try:
            print(f"尝试连接 Sentinel（第 {i+1} 次）...")
            sentinel = Sentinel(sentinel_hosts, socket_timeout=5)
            return sentinel
        except redis.ConnectionError:
            print("连接失败，重试中...")
            time.sleep(delay)
    raise Exception("无法连接到 Sentinel")

# 获取 Redis 连接
try:
    sentinel = connect_sentinel()

    # 获取 Master（写操作）
    master = sentinel.master_for('mymaster', socket_timeout=5, decode_responses=True)
    master.set('foo', 'bar')
    print("写入: foo -> bar")

    # 获取 Slave（读操作）
    slave = sentinel.slave_for('mymaster', socket_timeout=5, decode_responses=True)
    value = slave.get('foo')
    print(f"读取: foo -> {value}")

except Exception as e:
    print(f"发生错误: {e}")


