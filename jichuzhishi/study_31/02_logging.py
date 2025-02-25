# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:持久化到文件
    filename:指定输出文件
    filemode:默认追加；设置为"w"，清除在写入
"""

import logging

# 日志持久化:输出到文件中
# 使用basicConfig()方法的filename可以指定文件输出的文件，默认当前目录。没有则创建
logging.basicConfig(filename="demo.log",filemode="w",level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")