'''
当前模块要用本包中的模块和其它包中的模块
'''
# 用户发表文章
# 创建用户对象
# from .models import User#也可以使用“.“导入同级的模块
from package_test.models import User  # 即使要导入同级的其它模块，也要使用from
from models_package.models import Art

u = User('张三', '123456')
# 发表文章，文章对象
a = Art('个人总结', 'admin')
u.publish(a)

'''
里面的模块使用外面的模块
'''
list = [2, 3, 4, 5]
from caculate import add  # 导入包的时候都是从项目开始往下找，若是模块就在项目下，直接使用from

print(add(*list))
