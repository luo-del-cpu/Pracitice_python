# study_19
'''
文件上传
保存log

系统函数：
open（file，mode，buffering，encoding）,只能打开文件
1.open(path/filename,'rt')---->返回值：stream（流/管道）
2.container = stream.read（）---->读取管道中的内容

注意：如果传递的path/filename有误，则会报错：FileNotFoundError
     如果是图片则不能使用默认的读取方式，mode要改为mode=‘rb’
'''

strem = open(r'C:\Users\86176\Desktop\python\aa.txt')
# strem.read()
#
# result = strem.read()
# print(result)

# stream.readable()操作
# result_1 = strem.readable()  # 判断是否可以读取 True False
# print(result_1)  # 得出：True

# strem.readline()
while True:
    result_3 = strem.readline() #注意：此处的readline()表示一行一行的去读，每次只读取一行内容，
                                # 前提是在上方没有进行过read()操作，若是进行过read()操作，此处输出为空
    print(result_3)
    if not result_3:
        break

# stream.readlines()操作
# result_4 = strem.readlines() #读取文件中的每行后保存到列表中后返回一个列表
# print(result_4)
# for i in result_4:
#     print(i)

#stream.read()读取图片操作

# stream = open(r'C:\Users\86176\Desktop\python\文件夹的复制练习.png','rb') #注意此处读取图片时，要声明mode是rb,
#                                                               #否则使用默认的rt去读就会报错
# png = stream.read()
# print(png)







