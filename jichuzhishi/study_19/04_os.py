"""
模块：os.py
os.path:对系统内的文件进行操作
os.path.dirname(__file__):获取当前文件所在的文件目录（以字符串形式返回的一个绝对路径）
os.path.join(path,'aa.png'):返回的是一个拼接后(path与png)的新的路径；
如果是os.path.join(path1,path2,"aa.png")，则path2就是多一层目录
__file__表示当前文件
"""
import os

# 知道原文件名的情况：
with open(r'/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19/文件夹的复制练习/1/user.txt', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    path = os.path.dirname(__file__)  # 查找当前路径
    print("path:"+path)  # 打印当前路径：/Users/luoxin/workspace/Pracitice_python/jichuzhishi/study_19
    print(type(path))  # 返回的是一个str类型
    path_1 = os.path.join(path, 'user.txt')
    print(path_1)  # 打印拼接后的路径：C:\Users\86176\Desktop\python\pc练习\lianxi.py\study_19\a.png
    with open(path_1, 'wb') as wstream:
        wstream.write(container)
print('文件复制完成！')

# # 不知道原文件名但是保存名称不变的情况：
# with open(r'C:\Users\86176\Desktop\python\test.png', 'rb') as stream:
#     container = stream.read()  # 读取文件内容
#
#     print(stream.name)  # 打印当前stream的路径和文件名：C:\Users\86176\Desktop\python\文件夹的复制练习.png
#     file = stream.name
#     filename = file[file.rfind('\\') + 1:]  # 截取文件名
#
#     path = os.path.dirname(__file__)  # 查找当前路径
#     path_1 = os.path.join(path, filename)  # 以原名字保存
#
#     with open(path_1, 'wb') as wstream:
#         wstream.write(container)
# print('文件复制完成！')
