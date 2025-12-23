# @Time : 2023/8/31 22:58
# @Author : luoxin

"""
列表的函数：
"""

# 删除：remove()、pop()、clear()

# remove():删除第一个出现的元素，如果没有找见报异常
numbers = ['a', 'b', 'a', 'c']
numbers.remove('a')
print(numbers)
# 输出：['b', 'a', 'c']

"""
pop():
1：默认移除列表最后一个元素并且可以返回删除的值
2：也可以根据索引删除对应的元素
"""
numbers = ['a', 'b', 'a', 'c']
# res = numbers.pop()
# print(res)
# 输出：c

new_l = []
for _ in range(len(numbers)):
    new_l.append(numbers.pop())
print("----->",new_l)

# clear():清空列表
numbers = ['a', 'b', 'a', 'c']
numbers.clear()
print(numbers)
# 输出：[]

# reverse():翻转列表，改变原列表的结构
numbers = ['a', 'b', 'a', 'c']
numbers.reverse()
print(numbers)
# 输出：['c', 'a', 'b', 'a']

# 排序：sort()：改变原列表的结构，默认升序，加入reverse=True降序
numbers = [5, 3, 2, 6, 8, 1]
numbers.sort()
print(f"numbers---> {numbers}")
# 输出：[1, 2, 3, 5, 6, 8]


# 排序：sorted(): 生成新列表（对象）。默认升序排列,可加参数改为降序：sorted(seq,reverse=True)

paixu = [21, 33, 2, 4, 22, 5]
print(sorted(paixu))
print(f"paixu---> {paixu}")
paixu.sort()
print(paixu)
# 输出：[2, 4, 5, 21, 22, 33]

"""
排序加key。sort(key=None),sorted(key=None)
key指的是“映射函数”，一般是lambda函数
"""
words = ["apple", "kiwi", "banana"]
print(f"根据长度排序--->{sorted(words,key=len)}")

# 排字典
students = [
    {"name": "Tom", "score": 90},
    {"name": "Jerry", "score": 85}
]

print(f"根据scroe排序--->{sorted(students,key = lambda x: x['score'])}")

# 排元组
data = [("Tom", 90), ("Jerry", 85)]

print(f"根据第二个值排序--->{sorted(data,key=lambda x:x[1])}")

# 多条件排序:先按姓名升序,再按分数降序

data1 = [
    ("Tom", 90),
    ("Tom", 85),
    ("Jerry", 90)
]
print(f"多条件排序--->{sorted(data1,key=lambda x:(x[0],-x[1]))}")


# 统计：count()
numbers = [5, 3, 2, 6, 8, 1]
print(numbers.count(5))
# 输出：1
