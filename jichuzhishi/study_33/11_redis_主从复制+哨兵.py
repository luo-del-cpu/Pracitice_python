# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
redis的主从复制+哨兵：高可用的解决方案
    基础概念：
        自动主从切换：如果 Master 挂了，Sentinel 会选出一个 Slave 自动提升为 Master。
        监控与通知：可以检测 Redis 运行状态，并在异常时发出警告。
        高可用管理：支持故障转移（Failover）。
    步骤：
        1：在不同的服务器上配置哨兵配置文件sentinel.conf,如下：
            sentinel monitor mymaster 192.168.1.100 6379 2
            sentinel down-after-milliseconds mymaster 5000
            sentinel failover-timeout mymaster 60000
            注意：mymaser必须名称一致；
                sentinel monitor ... 2;2的意思代表至少2个同意，才进行故障转移。所以至少需要3个哨兵
        2：配置完成后，每个服务器启动redis服务：redis-server /etc/redis/redis.conf
        3：每个服务器，启动哨兵服务：redis-sentinel /etc/redis/sentinel.conf
        4：验证是否监控成功，在哨兵服务器执行：redis-cli -p 26379 sentinel master mymaster
        4：python代码实现，如下；
"""

import redis
from redis.sentinel import Sentinel

# 配置 Redis Sentinel 服务器（哨兵 IP 和端口）
sentinel_hosts = [
    ('192.168.1.200', 26379),
    ('192.168.1.201', 26379),
    ('192.168.1.202', 26379)
]

# 连接 Sentinel
sentinel = Sentinel(sentinel_hosts, socket_timeout=5)

# 获取当前的 Master 节点（用于写操作）
master = sentinel.master_for('mymaster', socket_timeout=5, decode_responses=True)

# 获取一个 Slave 节点（用于读操作，sentinel 会随机返回一个可用的从节点）
slave = sentinel.slave_for('mymaster', socket_timeout=5, decode_responses=True)

# 写入数据（Master）
master.set('foo', 'bar')
print("写入: foo -> bar")

# 读取数据（Slave）
value = slave.get('foo')
print(f"读取: foo -> {value}")

