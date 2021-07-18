import time
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from HwTestReport import HTMLTestReport

if __name__ == '__main__':
    # 注意：加载同级目录下要使用两个'../'
    suit = unittest.defaultTestLoader.discover('../oneday', pattern='test_*')
    # unittest.main(defaultTest='suit')
    # 生成html空的报告文件
    now = time.strftime('%Y%m%d%H%M%S',time.localtime())
    file = open('../report/report_'+str(now)+'.html', 'wb')
    # 初始化一个HTMLTestRunner的对象
    # runner = HTMLTestRunner(stream=file,title='测试报告',description='报告详情如下：')
    runner = HTMLTestReport(stream=file, title='测试报告', description='报告详情如下：',tester='T_Luo')
    runner.run(suit)
    # unittest.TextTestRunner(verbosity=2).run(suit)
