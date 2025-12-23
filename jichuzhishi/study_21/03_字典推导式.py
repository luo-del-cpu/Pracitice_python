# 字典推导式
dict1 = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}  # 若是有两个相同的Value值，则取最后一个Value的值
newdict = {value: key for key, value in dict1.items()}  # 表达式中的意思是：将value与key对调，生成一个新的字典
print(newdict)

my_dict = {"a": 3, "b": 1, "c": 2}
new_dict = {key:value for key,value in sorted(my_dict.items(),key=lambda x:x[1])}
print(new_dict)

"""
zip:用来把多个可迭代对象“按位置一一配对”
若是长度不一致，则以最短的为准
"""

names  = ["Tom", "Jerry", "Bob"]
scores = [90, 85, 100]

print(zip(names, scores)) # 返回的是一个迭代器，可别转化为列表或字典

result = dict(zip(names,scores))
print(result) # {'Tom': 90, 'Jerry': 85, 'Bob': 100}

result1 = list(zip(names,scores))
print(result1) # [('Tom', 90), ('Jerry', 85), ('Bob', 100)]