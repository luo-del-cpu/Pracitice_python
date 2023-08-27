'''
编写一个程序，找出列表中的最大值。如果列表为空，则打印出"列表为空"的消息。
'''

numbers = [23, 56, 12, 78, 45, 90]
if len(numbers)==0:
    print("列表为空")
else:
    max_value=numbers[0]
    for i in numbers:
        if i > max_value:
            max_value=i
    print("最大值:",max_value)

numbers = [23, 56, 12, 78, 45, 90]

max_value=numbers[0]
for i in numbers:
    if i>max_value:
        max_value=i
else:
    if len(numbers)==0:
        print("列表为空")
print("最大值",max_value)


print('*'*10,"这是第1题的分割线",'*'*10)

'''
编写一个程序，在给定的字符串中查找特定字符，并输出该字符在字符串中的索引。
如果未找到该字符，则打印出"字符未找到"的消息。
'''
message = 'Hello, World!'
char ='i'
for i,a in  enumerate(message):
    if a==char:
        print(f"找到了字符{char}，在第{i}的位置")
        break
else:
    print("未找到字符")

print('-'*30)

"""
上述的代码有缺陷；如果字符串2个相同的字符，那么只要找出来第一个字符的位置，就停止了，无法找到第二个字符，
因为有break的存在；
所以，如果想找出字符都存在的位置，那么就必须改变结构，如下所示：
"""
# 设置一个变量为false
found=True
for i,b in enumerate(message):
    #判断是否有相同的字符，如果有，就打印出来
    if b==char:
        print(f"找到了字符{char}，在第{i}的位置")
        #置为true后，就表示有相同的字符
        found = True
#如果found为false（另外可以证明并没有进入if的判断之内，就没有相同的字符，无法置为true，found依然为false），not found就是true，条件成立，就代表没有找到字符
if not found:
    print("未找到字符")

print('*'*10,"这是第2题的分割线",'*'*10)

"""
编写一个程序，检查一个整数是否为回文数（正向和反向读取相同）。
如果是回文数，则打印出"是回文数"的消息；否则，打印出"不是回文数"的消息。
"""
num = 101
num_1=str(num)
is_huiwen = False
for i in range(len(num_1)):
    if num_1[i]==num_1[-(i+1)]:
        is_huiwen = True
        break
if is_huiwen:
    print("是回文数")
else:
    print("不是回文数")

print('*'*10,"这是第3题的分割线",'*'*10)

'''
编写一个程序，计算从1到100之间（包括1和100）所有能被3整除的数字之和，并打印出结果。
'''
sum=0
for i in range(1,101):
    if i%3==0:
        sum+=i
print("和是:",sum)

print('*'*10,"这是第4题的分割线",'*'*10)

'''
编写一个程序，遍历一个字符串，统计其中每个字符出现的次数，并以字典的形式打印出结果。
'''
message = 'Hello, World!'
for i in message:
    pass

print('*'*10,"这是第5题的分割线",'*'*10)

'''
检查是否存在重复元素：
'''
numbers = [10, 4, 8, 20, 5, 3]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("存在重复元素:", numbers[i])
            break
    else:
        continue
    break
else:
    print("不存在重复元素")
