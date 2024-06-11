# 字典推导式
dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}  # 若是有两个相同的Value值，则取最后一个Value的值
newdict = {value: key for key, value in dict.items()}  # 表达式中的意思是：将value与key对调，生成一个新的字典
print(newdict)
