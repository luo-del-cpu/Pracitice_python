# s2 = {}
# s1 = set()
# list1 = [12,3,45,3,56,3,4,3,2,1]
# # print(set(list1))
# #
# # print(type(s1))
#
# # 增加
# # s1.add("hello")
# # s1.add("年后")
# # s1.add("123")
# # print(s1)
# #
# # t1 = ("增加1","增加2")
# #
# # s1.add(t1)
# # print(s1)
# #
# # s1.update(t1)
# # print(s1)
#
# #删除
#
# # s1 = {'年后', '123', '增加2', 'hello', ('增加1', '增加2'), '增加1'}
# # s1.remove('年后')
# # print(s1)
#
# """
# 练习：
# 1：产生一个1-20的随机数，去除里面的重复项
# 2：键盘输入一个元素，将此元素从不重复的集合中删除
# """
# import random
#
# #方式一
# # list2 = []
# #
# # for i in range(20):
# #     ran = random.randint(1,20)
# #     list2.append(ran)
# # set1 = set(list2)
# # print(list2)
# # print(set1)
# #
# # num = int(input("输入一个数字："))
# # set1.discard(num)
# # print(set1)
#
# #方式二
# # set2 = set()
# #
# # for i in range(20):
# #     ran = random.randint(1,20)
# #     set2.add(ran)
# # print(set2)
#
# #字符操作
#
set1 = {1,2,3,4,6}
print(id(set1))
set1.add("d")
print(set1)
print(id(set1))
# set2 = {1,2,3,4,5}
#
# set9 = set1 ^ set2
# print(set9)
#
# set8 = set1.union(set2)
# print(set8)
# set7 = set1 | set2
# print(set7)
#
# set3 = set1 - set2
# set4 = set1.difference(set2)
#
# set5 = set1 & set2
# set6 = set1.intersection(set2)
#
# print(set6)
# print(set5)
# print(set4)
# print(set3)

s = {1: "abc", 2: "def"}
str1 = str(s)
print(str1)
