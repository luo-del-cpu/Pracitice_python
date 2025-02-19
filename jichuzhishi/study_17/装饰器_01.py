# @Time : 2023/12/24 20:38
# @Author : luoxin
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
