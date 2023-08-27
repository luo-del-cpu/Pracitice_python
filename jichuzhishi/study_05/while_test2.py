'''
编写一个程序，使用while循环计算1到100之间所有数字的和。
'''

num =1
sum=0
while num<=100:
    sum+=num
    num+=1
print(f'1-100的和为:{sum}')

"""
编写一个程序，使用while循环找出一个列表中最大的元素。
"""
numbers = [24, 56, 12, 78, 45, 90]
max_value = numbers[0]
index=1
while index<len(numbers):
    if numbers[index] > max_value:
        max_value = numbers[index]
    index+=1
print(f'最大值是：{max_value}')

'''
编写一个程序，使用while循环反转一个给定的字符串。
'''
string = 'hello'
reverse_string = ""

index = len(string) - 1
while index >= 0:
    reverse_string += string[index]
    index -= 1

print(reverse_string)

'''
编写一个程序，使用while循环判断一个给定的年份是否为闰年。
'''

year = int(input("请输入一个年份："))

is_leap_year = False

while year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        break
    else:
        is_leap_year = True
    break

if is_leap_year:
    print(year, "是闰年")
else:
    print(year, "不是闰年")

