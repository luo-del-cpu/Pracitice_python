# @Time : 2025/2/22 04:51
# @Author : luoxin

def wrapper(func, *args, **kwargs):
    print("调用函数前")
    result = func(*args, **kwargs)  # 拆包参数传递给目标函数
    print("调用函数后")
    return result

def add(a, b):
    return a + b

print(wrapper(add, 3, 5))          # 输出 8
print(wrapper(add, a=2, b=10))     # 输出 12