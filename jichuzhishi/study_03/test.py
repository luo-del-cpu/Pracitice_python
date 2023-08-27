import random

ran = random.randint(1,10)
num = int(input("输入一个数字:"))
if ran == num:
    print("猜对了")
else:
    print("猜错了")