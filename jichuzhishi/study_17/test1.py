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

house()
