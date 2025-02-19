# @Time : 2023/11/12 23:06
# @Author : luoxin

"""
字典里面的函数：
items():它返回字典中 所有键值对 的视图对象，每个键值对以一个元组的形式存储。
values():方法返回字典中所有值的视图对象。它包含字典中每个键对应的值
keys():方法返回字典中所有键的视图对象。它包含字典中每个元素的键
"""

dict4 = {"张三": 90, "李四": 100, "王五": 80, "赵六": 70, }
print(dict4.items())  # 得出：dict_items([('张三', 90), ('李四', 100), ('王五', 80), ('赵六', 70)])

# 找出考试成绩大于90分的人

for key, value in dict4.items():
    print(key, value)
    if value > 90:
        print(key)

print(dict4.values())  # dict_values([90, 100, 80, 70])
print(dict4.keys())  # dict_keys(['张三', '李四', '王五', '赵六'])

# in也可以用于字典操作，用于判断元素有没有在字典的key中出现
