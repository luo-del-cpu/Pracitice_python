"""
系统函数：
open（file，mode，buffering，encoding）
1.open(path/filename,'rt')---->返回值：stream（流/管道）
    file：必需，表示要打开的文件的路径（可以是相对路径或绝对路径）。
    mode：可选，指定打开文件的模式（默认为 'r'，即只读模式）。
    buffering：可选，控制文件的缓冲策略。默认是 -1，表示使用默认的缓冲机制。
    encoding：可选，指定文件的编码（例如 'utf-8'）。如果不指定，系统默认使用平台的编码。

2.mode模式：
    'r'：读取（默认模式），如果文件不存在会抛出 FileNotFoundError 错误。
    'w'：写入，如果文件已存在会覆盖该文件，如果文件不存在则会创建新文件。
    'a'：追加，如果文件已存在，会在文件末尾追加内容；如果文件不存在，则创建新文件。
    'b'：以二进制模式打开文件（可以与其他模式组合使用，如 'rb' 或 'wb'）。
    'x'：创建并打开文件，如果文件已存在则抛出 FileExistsError 错误。
    't'：以文本模式打开文件（默认模式）。
    'r+'：读取和写入，文件必须存在。

3：stream.close() #释放资源，只有在释放资源之前才能进行读写操作，在这个之后无法进行读写操作

注意：如果传递的path/filename有误，则会报错：FileNotFoundError
     如果是图片则不能使用默认的读取方式，mode要改为mode=‘rb’
"""
# stream.read():读取文件的全部内容，返回所有内容
stream = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt')
print(stream.read())

print("*"*50)

# stream.readable()操作
result_1 = stream.readable()  # 判断是否可以读取 True False
print(result_1)  # 得出：True

print("*"*50)

# stream.readline():逐行读取
# while True:
#     result_3 = stream.readline() #注意：此处的readline()表示一行一行的去读，每次只读取一行内容，
#                                 # 前提是在上方没有进行过read()操作，若是进行过read()操作，此处输出为空
#     print(result_3)
#     if not result_3:
#         break

print("*"*50)

# stream.readlines()操作
result_4 = stream.readlines() #读取文件中的每行后保存到列表中后返回一个列表
print(result_4)
for i in result_4:
    print(i)

"""
解释：当你打开文件时，文件会有一个“指针”或游标，指示当前读取到文件的哪个位置。
每次调用 read() readline() 或 readlines() 时，文件指针会 向前移动，指向下一次读取的位置。
所以如果上方已经读取完文件，“指针”就会跑到最下面，后续读取就会什么都取不到。
"""

print("*"*50)

#stream.read()读取图片操作
#注意此处读取图片时，要声明mode是rb, #否则使用默认的rt去读就会报错
stream = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/a1.jpg','rb')
png = stream.read()
print(png) # 返回二进制数据

stream.close()






