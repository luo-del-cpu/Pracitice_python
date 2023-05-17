# 字典推导式
dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}  # 若是有两个相同的Value值，则取最后一个Value的值
newdict = {value: key for key, value in dict.items()}
print(newdict)
