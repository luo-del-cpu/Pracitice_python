# @Time : 2023/11/16 23:27
# @Author : luoxin
import random


def gerenate_random(nmber):  # 这里的number是"形参"
    for i in range(nmber):
        ran = random.randint(1, 20)
        print(ran)


gerenate_random(10)  # 这里的10是"实参"


# 判读是不是什么类型
tuple1 = tuple()
print(isinstance(tuple1,tuple)) #True:返回值是布尔类型
