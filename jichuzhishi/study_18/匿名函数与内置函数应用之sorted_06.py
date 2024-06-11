'''
sorted:
1.用法：sorted(Iterable,key = None,reverse = False)
2.sort和sorted的区别，sorted有返回值 sort没有
3.key传一个函数名：可以循环的都可以排序，字符串、字典、列表、元组
4.reverse = False默认为False升序排列；True降序排列
'''

list_1 = [2, 23, 4, 53, 555, 21]
a = sorted(list_1)
print(a) # [2, 4, 21, 23, 53, 555]

# 对年龄进行排序
list_3 = [
    {'name': 'tom', 'age': 18},
    {'name': 'lucy', 'age': 19},
    {'name': 'jack', 'age': 20}
]

b = sorted(list_3, key=lambda x: x['age'],reverse=True)  # 注意：需要按照条件查找字典中的元素时，lambda必须和key使用
print(b) # [{'name': 'jack', 'age': 20}, {'name': 'lucy', 'age': 19}, {'name': 'tom', 'age': 18}]


