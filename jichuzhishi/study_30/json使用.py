# @Time : 2024/9/9 22:05
# @Author : luoxin

"""
Python 内置了 json 模块，主要有四个常用方法：
    json.loads()：将 JSON 字符串转换为 Python 对象（反序列化）。
    json.dumps()：将 Python 对象转换为 JSON 字符串（序列化）。
    json.load()：从文件中读取 JSON 数据并转换为 Python 对象。
    json.dump()：将 Python 对象转换为 JSON 并写入文件。
"""

import json

# Python 对象
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}

# 序列化：Python 对象 -> JSON 字符串
json_str = json.dumps(data)
print(json_str)
# 输出：{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Science"]}

# 反序列化：JSON 字符串 -> Python 对象
python_data = json.loads(json_str)
print(python_data)
# 输出：{'name': 'Alice', 'age': 30, 'is_student': False, 'courses': ['Math', 'Science']}


with open('data.json', 'w') as f:
    # 使用 sort_keys 按字母排序
    # 使用 indent=4 进行格式化
    json.dump(data, f,indent=4,sort_keys=True)


with open('data.json', 'r') as f:
    python_data = json.load(f)
