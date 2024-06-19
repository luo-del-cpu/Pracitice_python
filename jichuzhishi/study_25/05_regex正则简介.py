import re

msg = '娜扎热巴佟丽娅'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)
print(result) # None,因为没有匹配，match是从头开始匹配

# 使用正则re模块方法：match
msg = '娜扎热巴佟丽娅'
result = re.match('佟丽娅', msg)
print(result)  # 得出：None，和上面的效果是一致的

# 使用正则re模块方法：search，找到一个就不继续往下找了
result = re.search('佟丽娅', msg)  # search进行正则字符串匹配方法，匹配的是整个字符串
print(result)  # 得出：<re.Match object; span=(4, 7), match='佟丽娅'>；span就是匹配的位置，match就是匹配内容
print(result.span())  # 得出：(4, 7)-->返回位置
print(result.group())  # 得出：佟丽娅-->提取到匹配的内容

