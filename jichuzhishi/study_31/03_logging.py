# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:向日志输出变量
"""

import logging

logging.basicConfig(level=logging.DEBUG)
name = "张三"
age = 18
# 如下两种是使用的debug中本身的方法，将变量传递给第一个参数
logging.debug("姓名：%s，年龄：%d","李四",20)
logging.debug("姓名：%s，年龄：%d",name,age)

# 如下的方式就是字符串的格式化，只使用了debug的第一个参数
logging.debug("姓名：%s，年龄：%d" %(name,age))
logging.debug(f"姓名：{name}，年龄：{age}")
