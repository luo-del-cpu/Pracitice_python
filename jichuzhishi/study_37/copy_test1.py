# @Time : 2025/12/10 22:34
# @Author : luoxin

import copy

import sys
print("启动文件：", sys.argv)

a = [1,[2,3]]
b = [1,[2,3]]

# 打印对象内存地址
print(id(a))
print(id(b))

# 对比是否引用同一个内存地址
print(a is b) # False


