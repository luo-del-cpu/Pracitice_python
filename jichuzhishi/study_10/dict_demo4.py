# @Time : 2023/11/13 23:07
# @Author : luoxin


"""
其余的内置函数：
update:拼接两个字典
fromkeys(seq,[default]):将seq转成字典的形式，如果没有指定默认的value则用None代替；如果指定default，则用defaylt代替
"""

dict1 = {'1': "第一", '2': "第二", '3': "第三", '4': "第四", }
dict2 = {'1': "替换的第一", '5': "第五"}
result = dict1.update(dict2)
print(result)  # None
print(dict1)  # {'1': '替换的第一', '2': '第二', '3': '第三', '4': '第四', '5': '第五'}

list1 = [1, 2, 3, 4]
print(dict.fromkeys(list1))  # {1: None, 2: None, 3: None, 4: None}
print(dict.fromkeys(list1, 10))  # {1: 10, 2: 10, 3: 10, 4: 10}
