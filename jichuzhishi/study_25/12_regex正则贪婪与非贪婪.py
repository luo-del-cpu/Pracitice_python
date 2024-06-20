# @Time : 2024/6/20 22:19
# @Author : luoxin
import re

msg = 'abc123abc'

# 默认两次都是贪婪模式，尽可能多的匹配
result = re.match('abc(\d+)',msg)
print(result) # <re.Match object; span=(0, 6), match='abc123'>

# 在两次后面加一个?，就表示非贪婪模式
result1 = re.match('abc(\d+?)',msg)
print(result1) # <re.Match object; span=(0, 4), match='abc1'>

