"""
reduce:
1.reduce函数会将可迭代对象中的值依次传入的函数中，函数会接收两个参数，用于做累加，累乘等操作
2.用时注意，需要提前导入模块
3.reduce（lambda x,y:x+y,可迭代的数据，initial=None）
"""
from functools import reduce

tuple_1 = (1, 2, 3, 4, 5)
c = reduce(lambda x, y: x + y, tuple_1)
print('c的值是：', c)  # 得出：15 （先去元组中的两个元素相加，将相加后的和继续从左往右继续累加下一个元素）

tuple_2 = (1,)
c_1 = reduce(lambda x_1, y_1: x_1 + y_1, tuple_2)
print('c_1的值是：', c_1)  # 得出：1 （注意：此处需要两个参数，但是元组中只有一个元素，这时候y就会默认传一个初始值None,也就是0）

tuple_2 = (1,)
c_2 = reduce(lambda x_2, y_2: x_2 -y_2, tuple_2,10) #注意：如果传入了 initial 值，
                                                    #那么首先传的就不是 sequence 的第一个和第二个元素，
                                                    # 而是 initial值和 第一个元素。经过这样的累计计算之后合并序列到一个单一返回值
print('c_2的值是：', c_2) #得出：9

tuple_3 = (1, 2, 3)
c_3 = reduce(lambda x_3, y_3: x_3 - y_3, tuple_3)
print('c_3的值是：', c_3) #得出：-4

tuple_3 = (1, 2, 3)
c_4 = reduce(lambda x_4, y_4: x_4 - y_4, tuple_3,10)
print('c_4的值是：', c_4) #得出：4

