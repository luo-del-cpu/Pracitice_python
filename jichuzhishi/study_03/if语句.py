"""
单层判断：
if 条件表达式：
    执行步骤
"""

# today_weather = "rainyday"
# if(today_weather == "rainyday"):
#     print("take your umbrella")

"""
双重判断：
if 条件表达式：
    执行步骤
else：
    执行步骤
"""
# gaokao_soccer = int(input("请输入高考分数："))
# #gaokao_soccer = 580
# if gaokao_soccer > 580 :
#     print("go 211")
# else:
#     print("go home")

"""
嵌套判断：
if 条件表达式：
    执行步骤
    if 条件表达式：
        执行步骤
    else：
        执行步骤
else：
    执行步骤
"""

# num = 2
# if num > 1 and num < 3:
#     print("这是一个小于3的数")
#     if num >3 and num <6:
#         print("这是一个小于6的数")
#     else:
#         print("这是一个大于6的数")
# else:
#     print("这是一个大于3的数")

"""
多层判断：
if 条件表达式：
    执行步骤
elif 条件表达式：
    执行步骤
else:
    执行步骤
"""

# level = int(input("请输入你的分数："))
# # if level > 10 and level < 30:
# #     print("C")
# # elif level >30 and level < 60:
# #     print("B")
# # else:
# #     print("A")

#while判断

# count = 0
# while count < 100 :
#     print("计数器：",count)
#     count += 1

# count = 0
# while count < 100 :
#     count += 1
#     if count < 20 and count >10:
#         continue
#     print("计数器：",count)


#死循环 dead loop
# while True :
#     print("死循环")

#猜年龄游戏
# import random
# n = random.randint(0,10)
# count = 0
# while count < 3:
#     user_gess = int(input("输入猜测的年龄值："))
#     if user_gess > n:
#         print("猜小一点")
#     elif user_gess < n :
#         print("猜大一点")
#     else:
#         print("你答对了")
#     count +=1
# print(n)

#猜黑姑娘年龄的游戏：
# for black_girl_old = int(input("猜一猜黑姑娘的年龄："))
# if black_girl_old > 25 :
#     print("猜的太大了，猜小点儿")
# elif black_girl_old < 20 :
#     print("猜的太小了，猜大点儿")
# elif black_girl_old == 25:
#     print("你猜对啦")

# level = input("输入等级(lv1,lv2)：")
# if level == 'lv1':
#     print('免费玩')
# else:
#     print("必须充钱；")
#     money = int(input("输入充值的金额："))
#     if money%100 == 0 and money > 0 :
#         print("已充值金额：",money)
#     else:
#         print("Game over")

# import random
# ran = random.randint(1,10)
# num = int(input("输入数字："))
# if num == ran :
#     print("猜对了")
# else:
#     print("猜错了")
# print("随机数：",ran)

# age = int(input('猜猜我的年龄：'))
# if age > 80 :
#     print("老年人")
# elif age >40 and age < 80 :
#     print("中年人")
# elif age < 18 :
#     print("未成年")