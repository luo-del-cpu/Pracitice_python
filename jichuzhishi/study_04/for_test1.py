"""
打印列表中的所有元素：
numbers = [1, 2, 3, 4, 5]
输出：1 2 3 4 5
"""

print("-----示例1-----")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print("-----示例2-----")

"""
计算列表中所有元素的和"
numbers = [1, 2, 3, 4, 5]
输出：15
"""
numbers = [1, 2, 3, 4, 5]
sum1 = 0
for i in  numbers:
    sum1+=i
print("所有数的和:",sum1)
print("使用sum求和:",sum(numbers))


print("-----示例3-----")

"""
打印字符串中每个字符及其对应的索引位置：
message = 'Hello, World!'
输出：
 H 0
 e 1
 l 2
 l 3
 o 4
 , 5
   6
 W 7
 o 8
 r 9
 l 10
 d 11
 ! 12
"""
message = 'Hello, World!'
for i,b in enumerate(message):#enumerate:枚举函数，可以列出迭代对象的索引与对应的值
    print(b,i)

sum2=0
for i in message:
    print('--->',i,sum2)
    sum2+=1


print("-----示例4-----")

"""
找出列表中的最大值并打印该值：
numbers = [23, 56, 12, 78, 45, 90]
输出：90
"""
numbers = [23, 56, 12, 78, 45, 90]
max_value = numbers[0]
for i in numbers:
    if i > max_value:
        max_value = i
print("最大值:",max_value)
print("使用max求最大值：",max(numbers))

print("-----示例5-----")


"""
统计字符串中某个字符出现的次数：
entence = 'I am learning Python programming.'
character = 'a'
输出：3
"""
entence = 'I am learning Python programming.'
character = 'a'

suma=0
for i in entence:
    if i==character:
        suma+=1
print("a出现的次数:",suma)
print("使用str.count()统计a出现次数：",entence.count('a'))
