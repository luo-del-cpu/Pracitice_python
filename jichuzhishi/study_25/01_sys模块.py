"""
当你导入一个模块，Python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录
3.如果都找不到，Python会查看默认路径、UNIX,默认路径一般为/usr/local/lib/python
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
"""

'''
自定义模块
系统模块
    sys
'''
import sys


print(sys.path)  # 打印找模块的路径

print(sys.version)  # 打印Python解释器版本

print(sys.argv) # 如果在命令行中执行：python xxx.py aaa,就会得到一个列表['xxx.py','aaa']



