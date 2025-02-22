# @Time : 2023/12/10 17:18
# @Author : luoxin


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("装饰器：在调用函数之前执行一些操作")
        result = original_function(*args, **kwargs)
        return result
    return wrapper_function

@decorator_function
def greet():
    print("你好！")

greet()

print("*"*50)

def decorater(f):
    def wrpper(*args,**kwargs):
        f("张三")
        print(id(f))
        print("装修房子")
    return wrpper

@decorater
def house(name):
    print(f"{name}在建造房子")
house()
print(id(house))

print("*"*50)

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # 【重点：调用原函数，因为原函数有返回值，这里必须有一个值来接收，如果只是写fun(*args,**kwargs);那么原函数的返回值就会丢弃】
        result = func(*args, **kwargs)
        end = time.time()
        print(result)
        print(f"Function {func.__name__} took {(end - start):.6f}s to execute")
        # 【重点：原函数如果有返回值，这里最好也加返回值进行透传原函数的值，很少会修改原函数的值】
        return result
    return wrapper
@measure_time
def my_function():
    time.sleep(1)
    return "执行函数"

x = my_function()  # 打印：Function my_function took 1.000798s to execute
print("x的值:"+ x)

print("*"*50)

def create(pos=None):
    if pos is None:
        pos = [0, 0]

    def go(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step

        pos[0] = new_x
        pos[1] = new_y
        print("go的函数地址", id(go))

        return pos

    return go


player = create()
x = player([1, 0], 10)
print(x)
# print("----",player([1, 0], 10))
# print("----",player([0, 1], 20))
# print("----",player([-1, 0], 10))
print("player的函数地址",id(player))

print("*"*50)

def test(a):
    #print(a)
    return a
x=test(1)
print(x)


def bad_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # 不保存返回值
        return 100  # 强制返回 100
    return wrapper

@bad_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # 输出 100（原函数的返回值被覆盖）