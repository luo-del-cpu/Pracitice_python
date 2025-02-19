"""
文件的复制
with 结合open使用可以帮助我们自动释放资源
"""


with open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test.txt', 'rb') as f:
    container = f.read()  # 读取文件内容
    print(container)
    with open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/test1.txt', 'wb') as f:
        f.write(container)
print('文件复制完成！')
