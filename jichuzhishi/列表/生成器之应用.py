# 进程  > 线程 > 协程 （一个进程里可以包含多个线程，一个线程里可以包含多个协程）
def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield None


def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None


g1 = task1(5)
g2 = task2(5)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break
