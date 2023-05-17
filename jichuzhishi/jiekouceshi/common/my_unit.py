import unittest


class MyUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('测试类之前的准备工作：连接数据库，创建日志对象')

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试类之后的扫尾工作：销毁数据库连接，销毁日志对象')

    def setUp(self) -> None:
        print('测试用例前的准备工作：打开浏览器，加载网页')

    def tearDown(self) -> None:
        print('测试用例后的扫尾工作：关闭浏览器')
