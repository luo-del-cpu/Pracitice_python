"""
sorted:
1.用法：sorted(Iterable,key = None,reverse = False)
2.sort和sorted的区别，sorted有返回值,但是不改变原有的列表； sort没有返回值，直接改变原列表
3.key传一个函数名：可以循环的都可以排序，字符串、字典、列表、元组
4.reverse = False默认为False升序排列；True降序排列
"""

list_1 = [2, 23, 4, 53, 555, 21]
a = sorted(list_1)
print(a) # [2, 4, 21, 23, 53, 555]

# 对年龄进行排序
list_3 = [
    {'name': 'tom', 'age': 18},
    {'name': 'lucy', 'age': 19},
    {'name': 'jack', 'age': 20}
]

"""
使用逻辑：
    sorted会迭代list3，迭代出来后，在lambda中将每个迭代的值当做x输入，然后取出x['age']的值进行比较
"""
b = sorted(list_3, key=lambda x: x['age'],reverse=True)  # 注意：需要按照条件查找字典中的元素时，lambda必须和key使用
print(b) # [{'name': 'jack', 'age': 20}, {'name': 'lucy', 'age': 19}, {'name': 'tom', 'age': 18}]

items = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
# 根据第二个元素排序
c = sorted(items,key=lambda x:x[1])
print(c) # 得出：[(1, 'apple'), (3, 'banana'), (2, 'cherry')]


# 对列表排序： 对列表中的字符串按长度排序
words = ['apple', 'banana', 'kiwi', 'cherry']
d = sorted(words,key=lambda x:len(x),reverse=True)
print(d) # 得出：['banana', 'cherry', 'apple', 'kiwi']

# 对字典的值排序
my_dict = {"a": 3, "b": 1, "c": 2}
e = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
print(e) # 得出：[('a', 3), ('c', 2), ('b', 1)]