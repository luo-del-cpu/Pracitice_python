# 定义类和属性

# 定义类
class Student():
    # 类属性
    name = 'zhangsan'
    age = '18'


# 使用类，创建对象
zhangsan = Student()
print(zhangsan.name)  # 得出：zhangsan；此处的逻辑就是先在对象自己的内存空间找有没有name属性，
# 没有则在类中找属性，有就打印，没有就报错

# 对象属性
zhangsan.age = 19  # 只要有赋值操作，就会在对象自己的内存空间先查找是否有相同的属性，有就覆盖，没有就创建一个对象属性
print(zhangsan.age)  # 得出：19 ；先在自己的空间里找age属性，有age属性，打印，不继续在类中找

# 修改类属性
Student.name = 'lisi'
wangwu = Student.name  # 得出：lisi;若要修改类属性，就必须使用类名去修改
print(wangwu)

p = Student()
print(p.name)
