# @Time : 2025/3/19 20:27
# @Author : luoxin


from collections import defaultdict

dict1 = [{"测试": 10}, {"测试1": 20}, {"测试3": 20}, {"测试": 30}]

# defaultdict 会自动创建 key 并赋值 []
result = defaultdict(list)
print(result)

for d in dict1:
    for key, value in d.items():
        result[key].append(value)  # 直接 append，不会报错

# 转换为普通字典
print(result)
dict2 = dict(result)

print(dict2) # {'测试': [10, 30], '测试1': [20], '测试3': [20]}

dict3 = [{"测试": 10}, {"测试1": 20}, {"测试3": 20}, {"测试": 30}]
result1 = {}
for d in dict3:
    for key, value in d.items():
        if key not in result1:
            result1[key] = []
        result1[key].append(value)

print(result1) # {'测试': [10, 30], '测试1': [20], '测试3': [20]}

from urllib.parse import parse_qs

# 输入的查询字符串
query_string = "xxxxabc=123&xxxxxbcd=234&xxxxdef=345"

# 使用 parse_qs 解析查询字符串
params = parse_qs(query_string)
print(params)

# 提取 "abc" 对应的值
abc_value = params.get('xxxxabc', [None])[0]

# 输出结果
print(abc_value)  # 输出: 123
