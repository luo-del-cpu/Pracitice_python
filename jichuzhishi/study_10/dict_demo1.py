# @Time : 2023/9/17 23:57
# @Author : luoxin

"""
字典：dict
1：符号：{}
2：关键字：dict
3：保存的元素是：key:value
"""

t1 = {}
t2 = dict()
# 上述都代表是空字典

dict1 = dict([('name', 'lucky'), ('age', '18')])  # 将列表或元组转换成字典时，必须是里面的元素是成对出现，否则报错
print(dict1)  # 输出：{'name': 'lucky', 'age': '18'}

dict2 = dict(a=1,b=2,c=3)
print(dict2) # {'a': 1, 'b': 2, 'c': 3}