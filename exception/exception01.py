# 语法错误和异常
# 异常：在程序运行的时候报出来的：...Error

# 异常处理
'''
格式：
try:
    可能出现异常的代码
expect:
    如果有异常执行的代码
finally：
    无论是否存在异常都会被执行的代码

情况1：
    try：
        有可能出现很多异常
    except 异常类型1：
        执行的代码
    except 异常类型2：
        执行的代码
    except Exception: #注意：如果是最大的层级的Exception要放在最后，否则其它异常的就不会被找到
        执行的代码

情况2：
    try：
        有可能出现很多异常
    except 异常类型1：
        执行的代码
    except 异常类型2：
        执行的代码
    except Exception as err:
        print(err) --->err的内容就是错误的原因

'''


def fun():
    try:
        n1 = int(input('输入第一个数字：'))
        n2 = int(input('输入第二个数字：'))
        per = input("输入运算符号： + — * /:")
        if per == '+':
            # 加法
            result = n1 + n2
        elif per == '_':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        print('结果是：', result)

    except ValueError:
        print('输入必须是数字！！！')
    except ZeroDivisionError:
        print('除数不能为0')
    except Exception as err:
        print('出错了！！！', err)


fun()
