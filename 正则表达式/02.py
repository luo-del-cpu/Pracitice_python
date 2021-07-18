import re

# 分组
# 匹配数字0-100之间
'''
'|':或者的意思
'()':将或者放入其中,例如：（w1|w2）w1或w2
'''
# 验证邮箱的输入：163 126 qq
s = '23234234@qq.com'
result = re.match(r'\w{5,10}@(162|126|qq)\.(com|cn)$', s)
print(result)

# 不是以4,7结尾的手机号码（11位）
phone = '12324243227'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result)  # 得出None

# 爬虫
phone_1 = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone_1)  # 此处加了（）表示进行了分组
print(result)

# 提取

# 提取所有
print(result.group())  # 得出：010-12345678
# 提取第一组
print(result.group(1))  # 得出：010
# 提取第二组
print(result.group(2))  # 得出：12345678
