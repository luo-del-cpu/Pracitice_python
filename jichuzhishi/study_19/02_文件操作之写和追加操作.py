"""
特点：
1.只要mode是‘w’表示的是写操作，每次执行都会删除原来的内容，如果文件不存在则会创建新文件。
2.方法
        write（写的内容） 每次都会把原来的内容清空，然后写当前的内容.返回写入的字符数（即写入的字节数）
        writelines(iterable) 可以放入可迭代的数据，自动迭代没有换行效果.没有返回值，即返回 None
        stream_1.writelines（[‘测试1\n’，‘测试2\n’]） --->换行效果需要自己手动加入
3.如果mode是‘a’表示追加操作，不会删除原内容
"""
stream_1 = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt', 'a')
result = stream_1.write('这是写入测试！')
print(result) # 7
stream_1.close()

stream_2 = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt', 'w')
result_2 = stream_2.write('这是第二个写入操作！')
stream_2.close()

stream_3 = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt', 'w')
result_3 = stream_3.writelines(['这是测试换行！\n','测试换行！\n'])
print(result_3) # None
stream_3.close()

stream_4 = open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt', 'a')
result_5 = stream_4.write('这是追加操作！\n')
result_6 = stream_4.write('这是追加操作1！\n')
print(result_5) # 8
stream_4.close() #释放资源，只有在释放资源之前才能进行读写操作，在这个之后无法进行读写操作