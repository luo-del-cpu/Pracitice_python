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
res = numbers.pop()
print(res)
# 输出：c

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

# 排序：sort()：改变原列表的结构
numbers = [5, 3, 2, 6, 8, 1]
numbers.sort()
print(numbers)
# 输出：[1, 2, 3, 5, 6, 8]

# 统计：count()
numbers = [5, 3, 2, 6, 8, 1]
print(numbers.count(5))
# 输出：1
