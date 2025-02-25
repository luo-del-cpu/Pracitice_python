# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:输出格式优化
    format = %()s

    logging 模块在生成日志记录时，会创建一个 LogRecord 对象，该对象包含以下 预定义的属性：

        %(asctime)s：日志生成时间（可格式化）--->2023-10-01 12:34:56,789
        %(levelname)s：日志级别名称（DEBUG/INFO等）--->DEBUG
        %(message)s：日志消息内容--->"This is a log message"
        %(name)s：Logger 的名称--->"root"
        %(filename)s：生成日志的源代码文件名--->"app.py"
        %(lineno)d：生成日志的代码行号--->42
        %(funcName)s：生成日志的函数名--->"main"
        这些字段名是 LogRecord 类的固定属性，直接对应日志记录的元数据，不能自定义名称。
"""

import logging
"""
不定义format输出：DEBUG:root:姓名：张三，年龄：18
定义format输出：姓名：张三，年龄：18
"""
logging.basicConfig(
    format=" %(asctime)s-%(levelname)s-%(filename)s: %(lineno)d-%(message)s",
    level=logging.DEBUG)
name = "张三"
age = 18
logging.debug(f"姓名：{name}，年龄：{age}")
