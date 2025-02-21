# 字典推导式
dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}  # 若是有两个相同的Value值，则取最后一个Value的值
newdict = {value: key for key, value in dict.items()}  # 表达式中的意思是：将value与key对调，生成一个新的字典
print(newdict)

my_dict = {"a": 3, "b": 1, "c": 2}
new_dict = {key:value for key,value in sorted(my_dict.items(),key=lambda x:x[1])}
print(new_dict)