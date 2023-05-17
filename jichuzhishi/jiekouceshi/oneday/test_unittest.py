import unittest

from ddt import ddt, data

from jiekouceshi.common.my_unit import MyUnit

@ddt
class TestUnittest(MyUnit):
    a = 19
    @data('测试data装饰器')
    # @unittest.skip('无条件忽略')
    def test_01_001(self):
        '''测试一'''
        print('测试1')

    # @unittest.skipIf(a>=16,'条件为True忽略')
    def test_01_002(self):
        '''测试二'''
        self.assertEqual(1, 2)
        print('测试2')

    # @unittest.skipUnless(a >= 20, '条件为False忽略')
    def test_01_003(self):
        '''测试三'''
        print('测试3')

if __name__ == '__main__':
    print('------------')
    unittest.main()
