# @Time : 2024/6/5 23:16
# @Author : luoxin

# try except finally
"""
情况1：
try：
    pass
except Exception as e:
    print(e)
finally:
    无论是否异常都会执行的代码

情况2：
def func():
    try:
        return 1
    except:
        return 2
    fianlly:
        return 3  # 只要finally中有return，就会覆盖上面的return返回的内容，无论是否有异常
"""
def func():
    stream = None  # 全局变量以便于finally中可以使用到
    try:
        stream = open('./test.txt')
        con = stream.read()
        print(con)
    except Exception as e:
        print(e)
    finally:
        print("--finally--")
        if stream:  # 此处最好是需要判断一下stream变量是否为有效值，否则可能引发报错从而掩盖上面真正的捕获的异常
            stream.close()  # 此处的stream无法直接使用，因为和try不是一个模块


# func()  # 输出：[Errno 2] No such file or directory: './test.txt' 和 --finally--

def func1():
    stream = None
    try:
        stream = open('./test.txt')
        con = stream.read()
        print("try")
        return 1
    except Exception as e:
        print(e)
        return 2
    finally:
        print("--finally--")
        if stream:
            stream.close()
        return 3
x = func1()
print(x) # 输出：[Errno 2] No such file or directory: './test.txt' 和 --finally-- 和 3
