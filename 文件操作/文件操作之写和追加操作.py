# 写文件

'''
特点：
1.只要mode是‘w’表示的是写操作，每次执行都会删除原来的内容
2.方法
        write（写的内容） 每次都会把原来的内容清空，然后写当前的内容
        writelines(iterable) 没有换行效果
        stream_1.writelines（[‘测试1\n’，‘测试2\n’]） --->换行效果需要自己手动加入
3.如果mode是‘a’表示追加操作，不会删除原内容
'''
stream_1 = open(r'C:\Users\86176\Desktop\python\test.txt', 'a')
#result = stream_1.write('这是写入测试！')
#result_2 = stream_1.write('这是第二个写入操作！')
#result_3 = stream_1.write('这是第三个写入操作！')
#result_4 = stream_1.writelines(['这是测试换行！\n','测试换行！\n'])
result_5 = stream_1.write('这是追加操作！\n')
result_6 = stream_1.write('这是追加操作1！\n')
print(result_5)

stream_1.close() #释放资源，只有在释放资源之前才能进行读写操作，在这个之后无法进行读写操作