# @Time : 2023/11/12 23:06
# @Author : luoxin

"""
字典里面的函数：
items():将字典的键值转换为列表保存
values():取出字典中所有的值，保存到列表中
keys():取出字典中所有的key,保存到列表中
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
