# @Time : 2024/6/5 22:53
# @Author : luoxin

# try except else
""""
情况1：
try:
    pass
except Exception as err:
    print(err)
else:
    没有异常才会执行的代码

情况2：
def ...:
    try：
            return ... # 如果try中有return，是不会执行下方的else的
    except Exception as err:
        print(err)
    else:
        执行的代码
"""


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('除数不能为0')
    except Exception as err:
        print(err)
    else:
        print('除法成功,结果是：', result)
    finally:
        print('这是finally模块，无论是否异常都会执行')


# divide(4, 2)  # 输出：除法成功,结果是： 2.0 和 这是finally模块，无论是否异常都会执行

# divide(4, 0)  # 输出：除数不能为0 和 这是finally模块，无论是否异常都会执行


def example_function():
    try:
        print("尝试执行")
        list1 = []
        list1.pop()
        return "从try返回"
    except Exception as e:
        print(f"捕获到异常: {e}")
        return "从except返回"
    else:
        print("else块被执行")
        return "从else返回"  # 这行代码实际上永远不会执行


# 调用函数并打印返回值
result = example_function()
print(result)  # 输出：尝试执行 捕获到异常: pop from empty list 和 从except返回
"""
当执行到 list1.pop时， 因为列表为空，解释器会抛出一个 pop from empty list 异常。
由于这个异常是在 try 块中抛出的，因此它会被紧随其后的 except Exception as e 块捕获。
一旦异常被捕获，程序的控制流就会立即跳转到 except 块中，执行 except 块中的代码。
由于 except 块中包含了一个 return 语句，该语句会立即终止函数的执行，并将控制权返回给调用者。
因此，try 块中 return "从try返回" 之后的代码（包括 else 块中的代码）都不会被执行。
"""
