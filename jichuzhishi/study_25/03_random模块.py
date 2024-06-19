# @Time : 2024/6/19 21:42
# @Author : luoxin

"""
random模块：


"""

import random

ran = random.random()  # 0-1之间的随机小数
print(ran)

ran = random.randrange(1, 10, 2)  # 包前不包后 (start,stop,step) 1-10 -->1,3,5,7,9
print(ran)

ran = random.randint(1, 10)  # 包含1和10

list = ['a', 'b', 'c']
ran1 = random.choice(list)  # 随机抽取一个

list1 = ['的', '地方', 'df']
ran2 = random.shuffle(list1)  # 打乱顺序
print(list1)
