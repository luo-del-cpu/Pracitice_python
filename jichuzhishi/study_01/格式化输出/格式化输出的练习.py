"""
1：使用%s占位，在使用 %()进行填充
"""
movie = "大侦探皮卡丘"
ticket = 45.9
count = 35
total = ticket * count
print("-------%s占位------>"+"电影：%s,票价：%s,总人数：%s"%(movie,ticket,count))


message = '''
电影：%s
票价：%.1f
人数：%d
总花费：%.2f
'''%(movie,ticket,count,total)
print("-------三引号保留格式输出------>"+message)

"""
2：使用{}占位，.format()进行填充
"""
ke_cheng = 'python'
day = 3
learn_day = 3
print("-------{}占位------>"+"我今天已经学习{}{}天了，接下来还有继续学习{}天".format(ke_cheng,day,learn_day))


# filename = 'picture.png'
# str = 'abcdefg'
# print(str[5:0:-1])
# print(filename[::-1])
# print(filename[8:-1])
# print(filename[:-2])
# print(filename[3:])
# print(filename[:7])
# print(filename[0])
# print(filename[0:7])
#
# str_1 = 'hello world'
# str = 'abcdefg'
# print(str_1[-1:-6:-1])
# print(str_1[:6])
# print(str_1[::-1])
# print(str_1[4:1:-1])
# print(str_1[2:8])
#
# print(str_1[::2])
# print(str[::2])
# print(str[-2:0:-1])


"""
3：使用f"{}"格式化输出
"""
name = '文件夹的复制练习'
print("-----使用f""{}""------->"+f"这是一个{name}")