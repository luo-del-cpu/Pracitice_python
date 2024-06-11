# @Time : 2023/11/14 23:08
# @Author : luoxin

"""
符号的操作：
in、==、-(差集)、&(交集)、|(并集)
"""
s1 = {1, 2, 3, 4, 5, 6}
print(1 in s1)  # True

s2 = {1, 2, 3, 4, 5, 6}
print(s1 == s2)  # True

s3 = {1, 2, 3, 4, 5, 6, 7}
s4 = s3 - s2
s5 = s2 - s3
print(s4)  # {7}
print(s5)  # set()：找出属于 s2 但不属于 s3 的元素

s6 = s3.difference(s2)
print(s6)  # {7}

s7 = s3 & s2
print(s7)  # {1, 2, 3, 4, 5, 6}
s8 = s3.intersection(s2)
print(s8)  # {1, 2, 3, 4, 5, 6}

s9 = s3 | s2
print(s9)  # {1, 2, 3, 4, 5, 6, 7}
s10 = s3.union(s2)
print(s10)  # {1, 2, 3, 4, 5, 6, 7}

"""
对称差集：^
"""

s2 = {1, 2, 3, 4, 5, 6}
s3 = {4, 5, 6, 7, 8}

# 找出两个集合的不同的元素
s4 = s2 ^ s3
print(s4)  # {1, 2, 3, 7, 8}
