# @Time : 2023/8/27 23:21
# @Author : luoxin

"""
字符串的切片操作：包前不包后
[start:end:方向与步长]:
1：表示从左至右
-1：表示从右至左并且倒序

str[0]:取下标第一个字符
str[0:7]:取下标第1个到第6个的字符
str[3:]:取下标第3个到末尾的字符
str[:7]:取从第0到第6个位子的字符
str[:-2]:取从第0到倒数第3个位子的字符
str[-2:]:取从倒数第2到最后的字符
str[3::-1]取下标为3个到开头倒序输出
str[:3:-1]取从末尾到下标为4的下一个倒序输出
str[::-1]:倒序输出
"""

s1='abc'
print(s1[-2:]) # bc

s2='hello world'
print(s2[-1:-6:-1]) #dlrow
print(s2[0:5]) # hello
print(s2[::-1]) # dlrow olleh
print(s2[4:1:-1]) # oll
print(s2[2:8]) # llo wo