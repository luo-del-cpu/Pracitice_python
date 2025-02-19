# @Time : 2025/2/19 14:15
# @Author : luoxin
"""
while 判断：(需要设置一个初始值和在循环中增加的值，否则循环可能会一直执行下去)
1：用于在满足特定条件时反复执行代码块。while 循环会持续执行，直到给定的条件为 False 为止。
2：在循环中根据某些条件提前退出。可以使用 break 来中断循环。
3：while continue：continue 用于跳过当前循环中的剩余代码，立即开始下一次迭代。
"""

# 1：基本while循环
count = 0
while count < 100 :
    print("计数器：",count)
    count += 1

# 2：while break终止循环

count1 = 0
while count1 < 100 :
    count1 += 1
    if count1 == 10:
        break
    print(count1) # 1-9

# 2：while continue跳出本次循环，进行下一次循环

count = 0
while count < 20 :
    count += 1
    if 15 > count > 10:
        continue
    print(count) # 1-10，,15-20


#死循环 dead loop
# while True :
#     print("死循环")

