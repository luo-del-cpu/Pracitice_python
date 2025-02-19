# @Time : 2023/11/12 22:37
# @Author : luoxin


"""
字典的添加与修改：
添加的格式：dict[key]=value
修改的格式：同上
"""
dict1 = {}
dict1["brand"] = "huawei"

print(dict1)

dict1["brand"] = "mi"

print(dict1)  # 当有同名的key重复添加时，就会覆盖；不同名的则新增

"""
字典的查询：
dict[key]:根据key获取value值，若是key不存在，则报错
dict.get('key'):根据key值获取value值，若是key不存在，不报错，返回None
dict.get('key',defalut):根据key值获取value值，如果取不到,则返回defalut的值
"""

dict3 = {"张三": 90, "李四": 100, "王五": 80, "赵六": 70, }
print(dict3['张三'])  # 得出：90
print(dict3.get("李四"))  # 得出：100
print(dict3.get("麻子", 20))  # 得出：20

"""
字典的删除：
del dict[key]:根据key删除
pop(['key',defalut]): 根据key删除字典中的键值对，返回值是删除的键的值；如果删除的是不存在的键，则返回默认值 
popitem():一般是从末尾开始逐个删除
clear():清空字典
"""

dict4 = {"张三": 90, "李四": 100, "王五": 80, "赵六": 70, }
del dict4['李四']
print(dict4)  # {'张三': 90, '王五': 80, '赵六': 70}

print(dict4.pop('王五'))  # 80
print(dict4.pop('麻子', 1000))  # 1000

"""
字典的遍历：
如果是单独遍历字典，那么得到的就是字典的key
"""

dict4 = {"张三": 90, "李四": 100, "王五": 80, "赵六": 70, }
for i in dict4:
    print(i)
# 得出：
# 张三
# 李四
# 王五
# 赵六
