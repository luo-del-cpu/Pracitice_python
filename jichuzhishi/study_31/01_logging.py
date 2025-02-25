# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:用于记录日志
    级别	使用场景
    DEBUG	开发调试细节（如变量值、中间步骤）
    INFO	程序运行关键节点（如服务启动、事务完成）
    WARNING	潜在问题但程序仍可运行（如配置缺省值）
    ERROR	严重错误导致功能失效（如数据库连接失败）
    CRITICAL	系统级错误（如磁盘满、内存耗尽）
"""

import logging

# 默认的日志输出级别为warning
# 使用basicConfig()来制定日志输出级别，将设置的日志级别及以上级别的日志都输出
# 注意：需要放在最开始，否则就会说在第一次调用logging的时候就隐式设置为waring级别
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")


