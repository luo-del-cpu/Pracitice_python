"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""

# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))

# if a >b:
#     a,b=b,a
# if a>c:
#     a,c=c,a
# if b>c:
#     b,c=c,b
# print(a,b,c)

# 从大到小排序
# if a <b:
#     a,b = b,a
# if a<c:
#     a,c=c,a
# if b<c:
#     b,c=c,b
# print(a,b,c)


"""
温度判断：编写一个程序，根据用户输入的温度值，判断并输出对应的天气状态。
例如，如果温度大于等于30度，输出"炎热的天气"；
如果温度在20到29度之间，输出"舒适的天气"；
如果温度在10到19度之间，输出"凉爽的天气"；
如果温度低于10度，输出"寒冷的天气"。
"""
tem = float(input("输入天气温度:"))

if tem >= 30:
    print("炎热的天气")
elif tem >=20 and tem <= 29:
    print("舒适的天气")
elif tem >=10 and tem <= 19:
    print("凉爽的天气")
elif tem <=10 :
    print("寒冷的天气")

""" 
分数等级：编写一个程序，根据用户输入的分数，判断并输出对应的等级。
假设满分为100分，90分及以上为"A"级，
80分及以上为"B"级，
70分及以上为"C"级，
60分及以上为"D"级，
60分以下为"E"级。
"""

score = int(input("输入分数:"))
if score >=90:
    print("成绩为A")
elif score>=80 and score <90:
    print("成绩为B")
elif score>=70 and score <80:
    print("成绩为C")
elif score>=60 and score <70:
    print("成绩为D")
else:
    print("不及格")

"""
年份判断：编写一个程序，根据用户输入的年份，判断该年份是否为闰年。
闰年的定义是可以被4整除但不能被100整除，或者可以被400整除。如果是闰年，则输出"是闰年"，否则输出"不是闰年"。
"""
year = int(input("输入年份:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("闰年")
else:
    print("不是闰年")

"""
购物折扣：编写一个程序，根据用户输入的购物金额和会员等级，计算并输出折后价格。
假设会员等级分为普通会员和VIP会员，普通会员没有折扣，
VIP会员有9折优惠。
例如，如果购物金额为100元，并选择VIP会员，输出90元。
"""
mon = int(input("输入购物金额:"))
lev = int(input("输入会员等级:"))

if lev >10:
    print(f"VIP会员，享受9折优惠，需要支付{mon*0.9}元")
else:
    print(f"普通会员，不享受优惠，需要支付{mon}元")



