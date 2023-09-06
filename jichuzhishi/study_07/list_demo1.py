# @Time : 2023/8/29 23:16
# @Author : luoxin

"""
list:列表
声明方式：[]
"""

"""
元素的获取方式：
使用索引进行获取
"""

names = ['a', 'b', 'c', 'd']
print(names[0])
# 输出：a
print(names[-1])
# 输出：d
print(len(names))
# 输出：4；列表中的元素个数

"""
结合循环
"""

for name in names:
    print(name, end='')
# 输出：abcd

"""
结合in判断
"""
if 'a' in names:
    print("存在")
else:
    print("不存在")
