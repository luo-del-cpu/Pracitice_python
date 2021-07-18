'''
生成器方法：
1.__next__():获取下一个元素；（具体事例见生成器）
2.send(value):向每次生成器调用中传值，注意：第一次调用send(None),必须先传入none
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp', temp)
        i += 1
    return '没有更多的数据！'


g = gen()
print(g.send(None))
n1 = g.send('哈哈')
print('n1:', n1)
n2 = g.send('呵呵')
print('n2:', n2)

