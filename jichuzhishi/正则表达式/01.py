import re

# msg = '娜扎热巴佟丽娅'
# pattern = re.compile('佟丽娅')
# result = pattern.match(msg)  # 没有匹配，因为match是从头开始匹配
# print(result)

# 使用正则re模块方法：match
# msg = '娜扎热巴佟丽娅'
# result = re.match('佟丽娅', msg)  # 得出：None
# print(result)
#
# result = re.search('佟丽娅', msg)  # search进行正则字符串匹配方法，匹配的是整个字符串
# print(result)  # 得出：<re.Match object; span=(4, 7), match='佟丽娅'>；span就是匹配的位置，match就是匹配内容
# print(result.span())  # 得出：(4, 7)-->返回位置
# print(result.group())  # 得出：佟丽娅-->提取到匹配的内容

# a2b h6k

# s = '哈哈33'
# result = re.search('[0-9][0-9]',s)
# print(result)
msg = 'safdadf5daffa8asdfa00'
result = re.search('[a-z][0-9][a-z]', msg)
print(result)  # 得出：<re.Match object; span=(6, 9), match='f5d'>；search只要找见第一个就不往下找了

result = re.findall('[a-z][0-9][a-z]', msg)
print(result)  # 得出：['f5d', 'a8a']；findall匹配整个字符串，找到匹配会继续找直到最后,最后放入一个列表中

# a7a a45f d0098df
msg = 'a7aasdfad88dfadfsd8888adf'
result = re.findall('[a-z][0-9]+[a-z]', msg)  # 得出：['a7a', 'd88d', 'd8888a']
print(result)

# QQ号码验证：5-11
qq = '34234234'
result = re.match('^[1-9][0-9]{4,10}$', qq)
print(result)

# 用户名可以是字母或者数字，不能是数字开头，用户名长度必须6位以上
# re.search('^[a-zA-Z][0-9a-zA-Z]{5,}$')

msg_1 = 'aa.py uu.txt bb.py cc.png'
# 找出“py”结尾的
print(re.findall(r'\w*\.py\b', msg_1))  # 一般正则中出现了\符号，在前面都加上r

