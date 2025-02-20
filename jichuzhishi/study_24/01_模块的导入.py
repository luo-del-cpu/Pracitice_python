"""
当此模块与其它包在同级的时候：
1.from 包 import 模块
2.from 模块 import 类|函数|变量【无需在加报名，可以直接调佣】
3.from 模块 import *【如果想限制获取的内容，可以子模块中使用__all__=[使用*可以访问到的内容 ]】
"""
# 使用包中模块中的User类
# from package_test import models  # 从包中导入模块
#
# u = models.User('admin', '123456')
# u.show()  # 得到：admin 123456

# from package_test.models import User  # 从包的模块中导入类
#
# u = User('admin', 123456)
# u.show()
# from models_package.models import Art
#
# a = Art('个人总结', '张三')
# a.show()

