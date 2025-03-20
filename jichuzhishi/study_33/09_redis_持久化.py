# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
redis持久化：将数据存储到磁盘上
    RDB模式（默认）；
        概述：
            RDB 是 Redis 的 快照（Snapshot） 方式持久化，
            它会在指定的时间间隔内，把内存中的数据保存为 二进制文件（.rdb）。
        配置：
            在 redis.conf 中，找到以下参数：
            save 900 1   # 900秒（15分钟）内至少1次修改
            save 300 10  # 300秒（5分钟）内至少10次修改
            save 60 10000 # 60秒（1分钟）内至少10000次修改
            这些参数的意思是：如果满足其中任意一个条件，Redis 就会触发 RDB 持久化。
        RDB 文件的默认存储路径：
            /var/lib/redis/dump.rdb  # Linux
    AOF模式：
        概述：
            AOF 采用 日志记录（Append-Only Log） 的方式，
            每当有写入命令（如 SET、DEL）时，都会追加到 appendonly.aof 文件中。
        配置：
            在 redis.conf 中，找到以下参数：
            appendonly yes  # 开启 AOF
            appendfilename "appendonly.aof"  # AOF 文件名
            AOF 提供 3 种 fsync（同步磁盘写入）策略：
            appendfsync always   # 每次写入都同步（最安全，但最慢）
            appendfsync everysec # 每秒写入一次（推荐，性能与安全折中）
            appendfsync no       # 由操作系统决定何时写入（最快，但风险最大）
    两者对比：
        	RDB（快照存储）	                    AOF（日志存储）
            数据安全	可能丢失最近修改的数据	        可靠，几乎无数据丢失
            恢复速度	快	                        慢（需执行所有命令）
            存储大小	小	                        大（记录所有操作）
            性能影响	低	                        高（持续写入日志）
            适用场景	适合定期备份、恢复速度快的场景	适合对数据安全要求高的场景
"""


