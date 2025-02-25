# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:以配置的方式使用方法：
    1：加载配置文件（如logging_bak.conf):具体配置要求已在logging.conf中说明
    2：获取记录器对象
    3：使用记录器记录日志
"""

import logging
import logging.config

# 加载配置文件
logging.config.fileConfig('logging_bak.conf')

rootLogger = logging.getLogger()
rootLogger.debug("This a root-debug message")

applogger = logging.getLogger('applog')
applogger.info("This is an applogger-info message")

print(__name__)