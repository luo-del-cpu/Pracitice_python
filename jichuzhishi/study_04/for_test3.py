'''
编写一个程序，查找列表中的第一个奇数，并输出该数字。如果列表中没有奇数，则打印出"列表中没有奇数"的消息
'''

numbers = [24, 56, 12, 78, 45, 90]
for i in  numbers:
    if i%2!=0:
        print(f"第一个奇数是{i}")
        break
else:
    print("列表中没有奇数")

"""
编写一个程序，查找字符串中的元音字母（a、e、i、o、u）并输出该字母。
如果字符串中没有元音字母，则打印出"字符串中没有元音字母"的消息。
"""
mes='ppl'
is_yuan = False
for i in mes:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(i)
        is_yuan = True
if not is_yuan:
    print("字符串中没有元音字母")

'''
编写一个程序，计算从1到100之间的所有整数之和。当和超过200时，停止计算并打印出当前的和。
'''
sum=0
for i in range(1,101):
    sum+=i
    if sum>200:
        print(sum)
        break