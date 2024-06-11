# @Time : 2024/6/5 22:10
# @Author : luoxin

# 语法错误与异常

# 语法错误：一般语法错误在pycharm中都会有一个红色的波浪线，可以避免

# 异常：指在真正运行的时候，才能发现的错误

# def chu(a, b):
#     return a / b
#
#
# chu(1, 0)  # 运行时会有报错：ZeroDivisionError: division by zero；此时下方的代码都不会执行

# 异常处理
"""
try：
    可能出现异常的代码
except：
    如果有异常执行的代码
finally： # 可有可无
    无论是否存在异常都会执行的代码

情况1：
try:
    pass
execpt 异常类型1:
    pass
execpt 异常类型2:
    pass
except Exception: # 一般此处的Exception放在最后，放在前面的话，因为包含了大多数的错误，所以放在前面的话不会走到其他的异常类型
    pass

情况2：
try：
    pass
except Exception as err:
    print(err)  # 打印出报错的详情信息
"""


def func():
    try:
        n1 = int(input("输入第一个数字："))
        n2 = int(input("输入第二个数字："))

        sum = n1 / n2
        print('和是：', sum)

        # 操作列表，为了制造一个错误
        list = []
        list.pop() # 因为列表为空，所以此处pop会报错

    except ValueError:  # try与except必须同时出现
        print('必须输入数字！')  # 如果输入不是数字，此处可以捕捉到，继续执行下方的内容
    except ZeroDivisionError:  # 如果除数为0，此处可以捕捉到，继续执行下方的内容
        print('除数不能为0')
    except Exception as err:  # 因为Exception属于最原始的父类，所以可以包含所有的错误；如果上面没有定义的err，都会进入到这个异常
        print('出错了', err)  # 此处另外定义了err,可以记录错误原因；例如上面的list.pop的错误就会打印出：出错了 pop from empty list


func()

print('-------->')  # 加入了try except后，即使报错，依然可以执行到此处
