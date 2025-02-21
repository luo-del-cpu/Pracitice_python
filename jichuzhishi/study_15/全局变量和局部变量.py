"""
global 变量的范围
局部变量 全局变量

局部变量：函数内部声明的变量，仅限在函数内部使用，外部无法使用

全局变量：1.申明在函数外层的是全局的，所有函数都可以访问
        2.如果要在函数内部【修改全局变量
            如果全局变量是不可变（例如：str、int、float、tuple、bool ）在函数中进行【修改需要添加global】；
            如果是可变的(例如：list、dict、set)，在函数中修改的时候就不需要加global

如果有同名的变量，那么会优先使用局部变量
"""

globals()  # 打印全局变量
locals()  # 打印当前位置的所有变量

