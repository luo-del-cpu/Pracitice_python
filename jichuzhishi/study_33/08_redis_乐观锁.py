# @Time : 2025/3/1 21:50
# @Author : luoxin

"""
WATCH 作用
    WATCH 监控指定的键，如果事务提交前该键被其他客户端修改，事务将取消执行。
    适用于 防止并发修改冲突，类似 乐观锁（Optimistic Locking）。
"""

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def transfer_money(sender, receiver, amount):
    while True:
        r.watch(sender)  # 监视 sender 账户
        balance = int(r.get(sender) or 0)  # 获取 sender 余额

        if balance < amount:
            print("余额不足，事务取消")
            r.unwatch()  # 取消监视
            return False

        pipe = r.pipeline()  # 开启事务
        pipe.multi()
        pipe.decr(sender, amount)  # 扣除 sender 账户余额
        pipe.incr(receiver, amount)  # 增加 receiver 账户余额
        try:
            pipe.execute()  # 提交事务
            print("转账成功")
            return True
        except redis.WatchError:
            print("检测到数据变更，重试...")
            continue  # 重新执行 while 循环，避免冲突

# 假设账户 A 有 100 元，账户 B 有 50 元
r.set("account:A", 100)
r.set("account:B", 50)

# 进行转账
transfer_money("account:A", "account:B", 30)

