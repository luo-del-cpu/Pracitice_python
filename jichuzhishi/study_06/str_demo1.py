# @Time : 2023/8/27 22:56
# @Author : luoxin
"""
字符串：
可以用''、""、""""""来定义

1：""""""是保留格式输出
2：可以使用 == 来比较两个字符串的内容是否相同
3：可以使用 is 来比较两个字符串的内存地址是否相同

"""

"""
字符串的运算符：+ *
+：相当于拼接符
*：相当于倍数
"""

s1 = 'abc'
s2 = 'de'

print(s1 + s2)
#输出：abcde

print(s1 * 4)
#输出：abcabcabcabc

"""
in：判断某个字符是否在另一个字符中，返回布尔类型的值（True/False）----只能判断连续的字符
not in：判断某个字符是否不在另一个字符中，返回布尔类型的值（True/False）----只能判断连续的字符
"""

print('a' in 'abc')
#输出：True
print('d' not in 'abc')
#输出：True

'''
字符串的格式化：%
用于字符串的格式化
'''

user = 'luoxin'
code = 'pythonr'
print('%s说：在学习%s'%(user,code))
#输出：luoxin说：在学习python

"""
r:保留原格式
有r：保留转义字符
无r：不保留转义字符
"""

print('%s说：\'哈哈哈\''%(user))
#输出：luoxin说：'哈哈哈'
print(r'%s说：\'哈哈哈\''%(user))
#输出：luoxin说：\'哈哈哈\'


