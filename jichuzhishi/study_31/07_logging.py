# @Time : 2025/2/23 16:33
# @Author : luoxin

"""
logging:
    在django实战项目中，更推荐在setting中定义LOGGING={},使用字典的方式解析。
    使得django项目在启动初始就会加载日志配置；假如现在这个文件就是django的项目
    settings文件。LOGGING={}的配置如下。
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simpleFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        # 控制台处理器（开发环境推荐）
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",          # 控制台显示所有 DEBUG 及以上日志
            "formatter": "simpleFormatter",
            "stream": "ext://sys.stdout"  # 明确指定输出到 stdout
        },
        # 文件处理器（生产环境推荐）
        "fileHandler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",            # 文件只记录 INFO 及以上日志
            "formatter": "simpleFormatter",
            "filename": "applog.log",
            "when": "midnight",         # 每天午夜切割日志
            "backupCount": 7,           # 保留最近7天日志（比原配置更合理）
            "encoding": "utf-8",
        }
    },
    "loggers": {
        "applog": {
            "level": "DEBUG",           # 记录器自身级别设为 DEBUG（最终输出级别由 handler 控制）
            "handlers": ["consoleHandler", "fileHandler"],
            "propagate": False
        }
    }
}