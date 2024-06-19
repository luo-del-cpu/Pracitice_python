# @Time : 2024/6/19 21:13
# @Author : luoxin
"""
time模块
重点：
    time()
    sleep()
    strftime('%Y-%m-%d %H:%M%S')
"""
import datetime
import time

# 1：时间戳

t = time.time()
print(t)  # 1718802862.456877

# 将时间戳转换成字符串
s = time.ctime()
print(s)  # Wed Jun 19 21:17:08 2024

# 将时间戳转成元祖
t = time.localtime()
print(
    t)  # time.struct_time(tm_year=2024, tm_mon=6, tm_mday=19, tm_hour=21, tm_min=18, tm_sec=34, tm_wday=2, tm_yday=171, tm_isdst=0)
print(t.tm_year)  # 2024

# 将时间戳转换成字符串
s = time.strftime('%Y-%m-%d %H:%M%S')
print(s)  # 2024-06-19 21:2244

# 2：睡眠
time.sleep(2)  # 睡眠2s

"""
datetime模块：
    time 时间
    date 日期
    datetime 日期时间
    timedelta 时间差
"""
print(datetime.date.today())  # 2024-06-19

# 时间差(必须创建一个对象获得)
timedel = datetime.timedelta(hours=2)

# 获取当前时间
now = datetime.datetime.now()

# 求出2小时之前的时间
result = now - timedel
print(result)  # 2024-06-19 19:35:31.868128
