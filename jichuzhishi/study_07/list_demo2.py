# @Time : 2023/8/29 23:31
# @Author : luoxin

"""
增删改查
"""

# 改：通过索引下标更改

names = ['tom', 'jack', 'lucy', 'henry']
names[-1] = 'modify'
print(names[-1])
# 输出：modify

for i in range(len(names)):
    if 'jack' in names[i]:
        names[i] = '杰克'
        break
print(names)
# 输出：['tom','杰克','lucy','henry']

# 删：使用del
names = ['tom', 'jack', 'lucys', 'lucy', 'henry']
name = 'lucy'

i = 0
l = len(names)

while i < l:
    if name in names[i]:
        del names[i]
        l -= 1
        continue
    i += 1
print(names)

# 添加：使用内置的函数进行添加：append、extend、insert
# append():末尾追加
girls = []
name1 = 'luoxin'

"""
注意：list.append不能再赋值给新的变量，否则会被覆盖为None；例如下方的:
girls = girls.append(name1)
如果这样写，就会将girl是重新赋值为None
"""
girls.append(name1)
print(girls)
# 输出：['luoxin']

# extend()：相当于列表的合并，把被添加的列表拆成一个个的元素加到要添加的列表中

names = ['a', 'b', 'c']
girls.extend(names)
print(girls)
# 输出：['luoxin', 'a', 'b', 'c']

print(names + girls)  # 等价于extend的用法

# insert():在想要插入的位置插入元素

cars = ['宝马', '奔驰', '路虎']
cars.insert(1, '法拉利')
print(cars)
# 输出：['宝马', '法拉利', '奔驰', '路虎']


