# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:以编程的方式(硬编码)使用方法；
    有4个核心组件：
        Logger(记录器)：应用程序直接调用的接口，负责创建日志记录（如 logger.debug()），并决定是否将日志传递给下一级组件。
        Handlers(处理器)：决定日志的输出目标（如控制台、文件、网络等），一个 Logger 可以绑定多个 Handler。
        Filters(过滤器):提供比日志级别更细粒度的控制，决定哪些日志需要被处理（例如过滤包含敏感信息的日志）。
        Formatters(格式化器):定义日志的输出格式（如时间、级别、消息内容等）。

        简单来说，就是把Logger理解为一根笔，用于记录；Handlers决定写在哪儿；Filters决定写的东西
        要过滤什么；Formatters决定写的格式是什么。
"""

"""
setLevel()：设置日志级别
"""
import logging

# 记录器
logger = logging.getLogger("app.log")
# 如果想要保持输出到控制台和文件是不同的级别日志，这里必须定义为DEBUG
logger.setLevel(logging.DEBUG)

# 处理器handler：StreamHandler:输出到控制台；FileHandler:输出到文件
# 若是没有给handler指定日志级别，将使用logger的级别
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('logfile.log')
fileHandler.setLevel(logging.INFO)

# formatter格式:可设置不同的格式给handler调用
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 记录器设置处理器:使用实例好的logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# filter过滤器:过滤记录器与处理器,将符合条件的进行输出；
#【注意：匹配是以前缀+.的方式匹配；如果条件是app,则logger的名字需要是：app.xxx】
flt = logging.Filter("app")

# 记录器关联过滤器
# logger.addFilter(flt)
# 处理器关联过滤器
fileHandler.addFilter(flt)


# 测试打印日志的代码
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")