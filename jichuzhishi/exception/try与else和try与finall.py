'''
注意：如果使用else则在try代码中不能出现return

异常情况4：
#study_19：stream = open（...）  stream.read()   stream.close()[在此处经常会忘记，所以将此放入finally里]
#数据库操作：同上文件操作所述一致

try：
    pass
expect：
    pass
fianlly:
    pass
'''


def fun():
    stream = None
    try:
        stream = open(r'C:\Users\86176\Desktop\python\p1\aa1.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----finally----')
        if stream:
            stream.close()
        #return 3  # 若是在finally里中加了return，则最终会返回出finally中的数据，会覆盖try中返回的数据


x = fun()
print(x)
