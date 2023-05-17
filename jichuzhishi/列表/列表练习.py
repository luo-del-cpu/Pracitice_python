 # #删除列表中所有包含“go”的元素
# words = ['hello', 'good bye', 'goods']
# w = input('输入单词：')
# i = 0
# l = len(words)
# while i < l:
#     if w in words[i]:
#         del words[i]
#         l -= 1
#         continue
#     i += 1
# print(words)


# a = [3, 4, 5, 6, 7, 9, 11, 13, 15,17]
# print(a[:5:-1])


# 产生一个随机数10个的列表，且都不相同
import random

i = 0
random_list = []
while i < 10:
    ran = random.randint(1, 20)
    if ran not in random_list:
        random_list.append(ran)
        i += 1
print(random_list)
print('----------------------')

max_value = random_list[0]
min_value = random_list[0]
sum_1 = 0
for value in random_list:
    #求列表中的最大值
    if value > max_value:
        max_value = value
    #求列表中的最小值
    if value < min_value:
        min_value = value
    #求列表中所有元素的和
    sum_1 += value
#打印出最大值、最小值、和
print(max_value, min_value, sum_1)
#使用内置函数验证最大值、最小值、和是否正确
print(max(random_list), min(random_list), sum(random_list))
