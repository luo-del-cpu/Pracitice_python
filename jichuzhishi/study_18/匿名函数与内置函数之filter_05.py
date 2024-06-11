'''
filter:
1.filter() 会根据判断结果自动过滤掉不符合条件的元素, 只返回由符合条件的元素组成的新列表(需要list一下).
2.与map()不同的是,filter()把传入的函数依次作用于每个元素, 然后根据返回值是True还是False来决定保留还是丢弃该元素.
3.filter(lambda x:x>10,可迭代的数据)
'''

list_1 = [1, 2, 34, 5, 6, 3]
a = filter(lambda x: x > 10, list_1)
print('a的值是：', list(a)) # [34]

list_3 = [
    {'name': 'tom', 'age': 18},
    {'name': 'lucy', 'age': 19},
    {'name': 'jack', 'age': 20}
]
b = filter(lambda x: x['age'] > 18, list_3)
print(list(b)) # [{'name': 'lucy', 'age': 19}, {'name': 'jack', 'age': 20}]

list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(lambda x: x % 2 == 1, list_4)
print(list(res)) # [1, 3, 5, 7, 9]


