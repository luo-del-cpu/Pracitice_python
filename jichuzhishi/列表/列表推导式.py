# 列表推导式：
# 旧的列表 --->新的列表

# 1.列表推导式：格式[表达式 for 变量 in 旧列表]或者[表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于或者等于3的人名
# names = ['tom', 'lily', 'abc', 'steven', 'bob', 'ha']
# result = [name for name in names if len(name) > 3]  # 此处len中的变量实际就是返回到新列表中的元素
# print(result)
#
# # 过滤掉长度小于或者等于3的人名并且将得到的名字首字母大写
# names = ['tom', 'lily', 'abc', 'steven', 'bob', 'ha']
# result = [name.capitalize() for name in names if len(name) > 3]
# print(result)
#
# # 将1-100之间能被3整除的数组成一个新列表
#
# newlist = [i for i in range(1, 101) if i % 3 == 0]
# print(newlist)
#
# # 构成一个列表：使用0-5之间的偶数，0-10之间的奇数--->[(偶数，奇数)。。。]
# newlist = [(x, y) for x in range(0, 5) if x % 2 == 0 for y in range(0, 10) if y % 2 != 0]
# print(newlist)
#
# # list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]] --->[3,6,9,5]
# list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
# newlist = [i[-1] for i in list]
# print(newlist)
#
# # if薪资大于5000加200，小于等于5000加500
dict1 = {'name': 'tom', 'money': 2000}
dict2 = {'name': 'jack', 'money': 5000}
dict3 = {'name': 'lily', 'money': 1000}
#
list_1 = [dict1, dict2, dict3]
#
# newlist = [person['money'] + 200 if person['money'] > 5000 else person['money'] + 500 for person in list_1]
# print(newlist)
# print(list_1)  # 此处注意没有修改原列表字典中的值；只是将运算后的结果存入一个新列表中，得到[2500, 5500, 1500]

newlist = [
    {'name': person['name'], 'money': person['money'] + 200} if person['money'] > 5000 else {'name': person['name'],
                                                                                             'money': person[
                                                                                                          'money'] + 500}
    for person in list_1]
print(newlist)
print(list_1)
