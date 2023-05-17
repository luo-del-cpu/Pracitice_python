# os.path中的函数
'''
# os.path.isabs()：判断路径是否为绝对路径，是返回'True',否则为’False‘
# os.path.isfile()：判断某一对象(需提供绝对路径)是否为文件
# os.path.isdir()：判断某一对象(需提供绝对路径)是否为目录
# os.path.dirname（）：获取路径
# os.path.abspath():通过相对路径得到绝对路径
# os.path.split(path):拆分路径返回到一个元组中，得到文件名
# os.path.splitext(path):分割文件与扩展名
# os.path.getsize(path):获取文件的大小，字节单位返回
'''
import os

# os.path.isabs()：判断路径是否为绝对路径，是返回'True',否则为’False‘
r = os.path.isabs(r'C:\Users\86176\Desktop\python')
print(r)  # True

r = os.path.isabs('a.png')  # 判断当前’a.png‘是否为绝对路径，因为此处‘os02.py’与’a.png’同级，可直接写
print(r)  # False

# os.path.isfile()：判断某一对象(需提供绝对路径)是否为文件
# os.path.isdir()：判断某一对象(需提供绝对路径)是否为目录


r = os.path.dirname(__file__)  # 获取当前文件的所在的文件夹路径（绝对路径）
b = os.path.dirname(r)
c = os.path.join(b,"aaa","111")
print(r)  # 得出：C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作
print(b)
print(c)

# os.path.abspath():通过相对路径得到绝对路径
r = os.path.abspath('a.png')
print(r)  # 得出：C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作\a.png

r = os.path.abspath(__file__)  # 获取当前文件的绝对路径
print(r)  # 得出：C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作\os02.py

r = os.getcwd()  # 与os.path.dirname()相同
print(r)  # 得出：C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作

# os.path.split(path):拆分路径返回到一个元组中，得到文件名
path = r'C:\Users\86176\Desktop\python\pc练习\lianxi.py\文件操作\os02.py'
r = os.path.split(path)
print(r)  # 得出：('C:\\Users\\86176\\Desktop\\python\\pc练习\\lianxi.py\\文件操作', 'os02.py')
print(r[1])  # 得出：os02.py

# os.path.splitext(path):分割文件与扩展名
r = os.path.splitext(path)
print(r)  # 得出: ('C:\\Users\\86176\\Desktop\\python\\pc练习\\lianxi.py\\文件操作\\os02', '.py')

# os.path.getsize(path):获取文件的大小，字节单位返回
r = os.path.getsize(path)
print(r)  # 得出：1668


