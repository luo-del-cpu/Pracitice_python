# @Time : 2025/2/27 13:48
# @Author : luoxin


"""
rabbitmq使用的前提是需要安装服务端的，在服务端启动后，可以在客户端操作；我们在python中
写的代码就相当于客户端使用，客户端使用需要使用pika
"""

import pika

# 创建一个连接
# 无密码码的
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# 有密码的
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='hello')

# 往队列中放入数据
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

# 关闭连接
connection.close()