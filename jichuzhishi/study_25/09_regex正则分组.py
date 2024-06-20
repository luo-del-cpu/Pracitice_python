import re

'''
'|':或者的意思
'()':将或者放入其中,例如：（w1|w2）w1或w2，一个括号代表一个分组
 使用()分组后，在使用group(1),group(2) 来提取分组中的内容
'''

"""
案例1：
    匹配数字0-100之间,不能以0开头
"""

n = '39'
# ? 代表匹配0或1次
# [1-9]?\d?$：卡住了1位数和2位数；
# 100$：卡住了100
# |：代表或者，匹配任意一个都生效
result = re.match('[1-9]?\d?$| 100$', n)
print(result)

"""
案例2：
    验证邮箱的输入：
    1：不同的邮箱：163 126 qq
    2：不同的后缀：com cn
    3：5-10位，字母与数字的组合
"""
s = '23234234@qq.com'
# (word|word|word) 表示的是整体的去比较；[abc]表示的是里面的每个元素
result = re.match(r'\w{5,10}@(162|126|qq)\.(com|cn)$', s)
print(result)

"""
案例3：
    1:不是以4,7结尾的手机号码
    2:11位
"""

phone = '12324243227'
# [0-35-689] 将不需要的数字4和7排除不写
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result)  # 因为是以7结尾，所以得出None

"""
案例4：
    提取区号
    1：前面的有可能3位或4位
    2：后面的是一个整体
"""
phone_1 = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone_1)  # 此处加了（）表示进行了分组
print(result)  # <re.Match object; span=(0, 12), match='010-12345678'>

# 提取所有
print(result.group())  # 得出：010-12345678
# 提取第一组
print(result.group(1))  # 得出：010
# 提取第二组
print(result.group(2))  # 得出：12345678

"""
案例5：
    在<html>abc</html>中进行提取
"""
msg = '<html>abc</html>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>',msg)
print(result)

# 提取中间的字符,因为只有一个(),所以group(1)即可
print(result.group(1))

