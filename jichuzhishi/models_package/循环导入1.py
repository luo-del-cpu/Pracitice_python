'''
循环导入：大型的python中，需要很多的模块，由于架构不当，出现了循环导入的问题
    A模块
        def 文件夹的复制练习():
            f()
    B模块：
        def f():
            文件夹的复制练习()

避免产生循环导入
1.重新架构
2.将导入的语句放入函数里面
3.把导入语句放在模块的最后
'''
from models_package.循环导入2 import func


def test1():
    print('---test1---')
def test2():
    print('---test2---')
    func()
test1()