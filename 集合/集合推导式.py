# 集合推导式：{}类似于列表推导式，在列表推导式的基础上做了去重操作
list = [1, 2, 3, 2, 3, 4, 5, 8, 8]

set_1 = {x for x in list}
print(set_1)
