import unittest

from ddt import ddt, data, unpack

from jiekouceshi.common.my_unit import MyUnit


@ddt
class TestPytest(MyUnit):
    @data("测试data装饰器")
    def test_01_baili(self, args):
        '''测试四'''
        print('测试pytest')
        print(args)

    @data("测试1","测试2")
    def test_01_baili(self, args):
        '''测试四'''
        print('测试pytest')
        print(args)

    @data(("测试1", "测试2"))
    @unpack
    def test_01_baili(self, args,args1):
        '''测试四'''
        print('测试pytest')
        print(args,args1)

    @data({"name":"测试", "age":"20"})
    @unpack
    def test_01_baili(self,name, age):
        '''测试四'''
        print('测试pytest')
        print(name, age)

if __name__ == '__main__':
    unittest.main()
