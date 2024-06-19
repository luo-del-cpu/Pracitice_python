# @Time : 2024/6/19 23:06
# @Author : luoxin

import re
"""
[]:代表一个范围，要匹配的内容。例如[a-z],代表a到z之间的字母
"""
s = '哈哈33'
result = re.search('[0-9][0-9]',s) # 代表是连续的两个0-9之间的数字搜索出来
print(result)


"""
案例：
    a2b h6k 在msg中搜索出上述格式的内容

search():只要找见第一个就不往下找了
findall():findall匹配整个字符串，会一直找到匹配的直到最后,最后放入一个列表中
"""
msg = 'safdadf5daffa8asdfa00'
result = re.search('[a-z][0-9][a-z]', msg)
print(result)  # 得出：<re.Match object; span=(6, 9), match='f5d'>；

result = re.findall('[a-z][0-9][a-z]', msg)
print(result)  # 得出：['f5d', 'a8a']；


