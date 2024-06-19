class A():
    def test(self):
        print('aaaa')


class B():
    def test1(self):
        print('bbbb')


class C(A, B):
    def test2(self):
        print('cccc')


c = C()
c.test()
c.test1()
c.test2()  # c继承了父类所有的方法
'''
python中允许多继承
    def 子类（A,B,C）:
        pass
    搜索原则：
        python3:广度优先
        python2:从左至右，深度优先 
'''
