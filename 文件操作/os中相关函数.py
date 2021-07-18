# os中的函数
'''
os.getcwd():获取当前目录
os.listdir():浏览文件夹
os.mkdir():创建文件夹
os.rmdir():删除文件夹（前提是文件夹中无文件）
os.chdir():切换目录
os.remove():删除文件
'''

import os

dir = os.getcwd()
print(dir)

# os.listdir(path): 返回指定目录（path）下的所有的文件和文件夹，保存到列表中
r = os.listdir(r'C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作')
print(r)  # 得出：['a.png', 'os01.py', 'os02（os.path相关函数）‘...]

# os.mkdir(path) :指定目录下创建文件夹
# r = os.mkdir(r'C:\Users\86176\Desktop\python\p1\p2')
# print(r)

# os.rmdir(path):删除文件夹（只能删除空文件夹）
# os.remove(/path/aa.txt):删除文件
# os.chdir():改变目录(相当于linux中的cd操作)

r'''
C:\Users\86176\Desktop\python\p1\p2目录下有多个文件，现在要求删除p2目录
'''
path = r'C:\Users\86176\Desktop\python\p1\p2'
p2_list = os.listdir(path)
for i in p2_list:
    path_1 = os.path.join(path, i)
    os.remove(path_1)
else:
    os.rmdir(path)
print("删除成功！")
