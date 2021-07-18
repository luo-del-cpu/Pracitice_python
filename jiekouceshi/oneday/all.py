import unittest
from jiekouceshi.oneday.test_unittest import TestUnittest

if __name__ == '__main__':
    # 创建一个测试套件
    suit = unittest.TestSuite()
    # 通过测试套件加载测试用例
    testcase = [TestUnittest('test_01_001'),TestUnittest('test_01_002'),TestUnittest('test_01_003')]
    suit.addTests(testcase)
    # suit.addTest(TestUnittest('test_01_001'))
    # suit.addTest(TestUnittest('test_01_002'))
    # 运行(使用套件可以指定运行的测试用例，如果不是用套件，则默认运行所有的用例)
    unittest.main(defaultTest='suit')
