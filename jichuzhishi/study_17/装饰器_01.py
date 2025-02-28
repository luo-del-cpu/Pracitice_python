# @Time : 2023/12/24 20:38
# @Author : luoxin
"""
装饰器:
    定义：
        装饰器的原理其实就是高阶函数和闭包的应用。
        装饰器函数接收一个函数作为参数，然后返回一个新的函数。这个新函数通常会包裹原函数，添加额外的功能。
    核心目的：
        是增强功能，而非改变原函数行为
    应用场景：
        1. 日志记录：记录函数的调用信息、参数、返回值等。

        2. 权限校验：检查用户是否有权限执行某个函数。

        3. 性能测试：计算函数的执行时间。

        4. 缓存：缓存函数的结果，避免重复计算。

        5. 事务处理：例如数据库事务，函数执行前开启事务，执行后提交或回滚。

        6. 路由注册：比如在web框架中，用装饰器将URL路径和处理函数关联起来。
"""
def decorater(f):
    def wrapper(*args, **kwargs):
        f("张三")
        print("f()函数地址:", id(f))
        print("wrapper()函数地址:", id(wrapper))
        print("被装饰过后的house()函数地址:", id(house))
        print("装修房子")
    return wrapper

@decorater
def house(name):
    print(f"{name}在建造房子")

"""
执行步骤:
1：从上至下执行代码，发现有decorater函数，系统加载装饰器函数，开辟内存空间
2：house被装饰函数作为参数传递给装饰器decorater，开始调用装饰器内部的代码
3：装饰器内部代码被执行的时候，就加载了wrapper函数，开辟内存空间
4：返回wrapper，被house()接收到

"""

house()
