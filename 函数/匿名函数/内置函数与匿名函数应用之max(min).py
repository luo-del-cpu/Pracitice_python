# 匿名函数与内置函数的结合使用
# max(min) sorted zip map reduce filter...

'''
max(min):
根据条件查找最大值，一般用在元素为字典的情况下：
max(可迭代的数据，key=lambda x : x['条件'])
'''

# 打印列表中的最大值
list_1 = [2, 3, 5, 6, 7]
m = max(list_1)
print('列表中的最大值是：', m)

# 打印列表中是字典元素中的最大/小值
list_2 = [{'a': 10, 'b': '21'}, {'a': 20, 'b': '22'}, {'a': 30, 'b': '20'}]

n = max(list_2, key=lambda x_1: x_1['b'])
print('列表中的最大值是：', n)  # 得出：{'a': 20, 'b': '22'}，实际返回的还是x_1参数

v = min(list_2, key=lambda x_2: x_2['a'])
print('列表的最小值是：', v)
list_3 = [
    {'name': 'tom', 'age': 18},
    {'name': 'lucy', 'age': 19},
    {'name': 'jack', 'age': 20}
]
d = max(list_3, key=lambda dic: dic['age'])  # lambda dic: dic['age']作为参数传递给max;x_3就表示从列表中取出的每一个元素（字典）
print('年龄最大的是：', d)  # 得出：{'name': 'jack', 'age': 20}，实际返回的是迭代出来的元素

list_4 = {'k1': '18', 'k2': '17'}
c = max(list_4, key=lambda x: list_4[x])  # 在这里，迭代list_4，先取k1作为参数传入匿名函数，经过list_4[x]处理得到18；
# 同理，继续使用K2作为参数，得出17，比较后得出k1比较大
c_1 = max(list_4, key=lambda x: x)  # 此处得到K2比较大；因为迭代list_4,先取K1作为参数传入匿名函数，表达式返回的还是x-->即K1
# 同理，继续使用K2作为参数，表达式返回的是K2,比较（根据ASCILL码值）得出K2较大
print('年龄最大的是：', c)  # 得出：k1 实际返回的是迭代出来的参数
print('对照组得出：', c_1)

print('---------------')
num = [10, 11, 12]
print(max(num, key=lambda i: i * i))

