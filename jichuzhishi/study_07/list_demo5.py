# @Time : 2023/9/12 22:33
# @Author : luoxin

"""enumerate():
枚举函数：用于将一个可遍历的数据对象（如列表、元祖或字符串）组合为一个索引序列
"""

l1 = ['a','b','c','d']
students = [
    {"name": "Tom", "score": 90},
    {"name": "Jerry", "score": 85}
]

for index,value in enumerate(l1):
    print(index,value)

"""
输出：
0 a
1 b
2 c
3 d
"""