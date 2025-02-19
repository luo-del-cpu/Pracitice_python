import random


"""
randint:生成一个指定范围内的随机整数
包前包后
"""
ran = random.randint(1,10)
num = int(input("输入一个数字:"))
if ran == num:
    print("猜对了")
else:
    print("猜错了")

"""
range函数：生成一个固定范围内的连续整数序列	
range（start,stop,step）:包前不包后
例如：
range(0,3):产生0 1 2 
range(4)：产生0 1 2 3
range(0,10,2)：产生0 2 4 6 8 
"""

·