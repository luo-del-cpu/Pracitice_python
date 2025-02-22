# @Time : 2023/12/10 17:18
# @Author : luoxin
"""
两种情况：
    原函数无返回值（return）
    原函数有返回值（return）
"""
import time

"""
原函数有返回值：
    原函数有返回值的情况下，需要在装饰器中调用原函数并且保留result，将result返回，保持透传。
    如果没有特殊需求，一般不会修改原函数的return result，保留与原函数一致；
    除非有特殊需求，才会修改返回值，例如：return 100 ，强制将原函数的返回值进行了修改
"""
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


"""
原函数没有返回值：
    即使原函数没有显式返回值（即默认返回 None），装饰器中的 result = original_function(...) 和 return result 依然是必要且安全的。
    原函数无返回值时的行为
        原函数 greet 没有 return 语句，默认返回 None。
        
        装饰器中的 original_function(*args, **kwargs) 会执行原函数，并捕获其返回值（即 None）。
        
        装饰器通过 return result 将 None 透传给调用者。
"""
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("装饰器：在调用函数之前执行一些操作")
        result = original_function(*args, **kwargs)
        print(f"result的值是: {result}") # 输出None
        return result
    return wrapper_function

@decorator_function
def greet():
    print("你好！")

greet()

print("*"*50)
"""
如下所示，就是在装饰器中不保存返回值，并且强行修改原函数的值；一般不建议这么做
"""
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # 不保存返回值
        return 100  # 强制返回 100
    return wrapper

@bad_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # 输出 100（原函数的返回值被覆盖）