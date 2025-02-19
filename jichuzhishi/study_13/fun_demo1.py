# @Time : 2023/11/16 23:27
# @Author : luoxin
import random

def test(n):
    print(n)

list1 = [1,2,3,4]
test(list1) # [1, 2, 3, 4] 整体传入

def generate_random(nmber):  # 这里的number是"形参"
    for i in range(nmber):
        ran = random.randint(1, 20)
        print(ran)


generate_random(10)  # 这里的10是"实参"


# isinstance():判断类型的方法
tuple1 = tuple()
print(isinstance(tuple1,tuple)) #True:返回值是布尔类型
