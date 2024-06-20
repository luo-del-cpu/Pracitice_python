# @Time : 2024/6/20 22:00
# @Author : luoxin

import re

"""
案例1：
    引用
    1：在<html>abc</html>中进行提取
    2：在'<html><h1>abc</h1></html>'中进行提取
"""
msg = '<html>abc</html>'

# \1 代表引用第1个分组里的内容
result1 = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg)
print(result1) # <re.Match object; span=(0, 16), match='<html>abc</html>'>

# 提取不同的group
print(result1.group(1)) # html
print(result1.group(2)) # abc

msg1 = '<html><h1>abc</h1></html>'

# </\2> 代表引用第2个分组的内容
result2 = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg1)
print(result2) # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>

"""
案例2：
    使用起名的方式代替 1 2分组的引用
使用方式：
起名：(?P<name>)
使用：(?P=name)
"""
msg2 = '<html><h1>abc</h1></html>'


result3 = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>$',msg1)
print(result3) # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>
