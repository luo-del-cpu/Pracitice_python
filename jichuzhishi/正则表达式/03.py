# sub函数：替换
# sub（正则表达式，‘新内容‘，string）
import re

result = re.sub(r'\d+', '90', 'java:100,python:100')
print(result)  # 得出：java:90,python:90

# split:切割
result = re.split(r'[,:]', 'java:100,python:100')
print(result)  # 得出：'java', '100', 'python', '100']
