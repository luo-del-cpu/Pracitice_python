# @Time : 2023/8/30 23:12
# @Author : luoxin

"""
生成10个不同的随机数放在一个列表中：
"""
import random

numbers = []
i=0
while i <10:
    ran = random.randint(1,20)
    if ran not in numbers:
        numbers.append(ran)
        i+=1
print(numbers)

"""
在一个列表中找出最大值、最小值
"""
maxvalue = numbers[0]
minvalue = numbers[0]

for value in numbers:
    if value > maxvalue:
        maxvalue = value
    if value < minvalue:
        minvalue = value
print(f"最大值是{maxvalue}，最小值是{minvalue}")

"""
冒泡排序
"""

numbers = [15, 13, 8, 20, 12, 19, 1, 9, 16, 5]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i],numbers[j] = numbers[j],numbers[i]
print(numbers)
