# @Time : 2025/2/27 13:48
# @Author : luoxin

"""
交换机的fanout模式
    定义发布者:
        1：创建连接
        2：定义交换机,与消费者的交换机的名称需要一一致，定义交换机类型
        3：放入消息
"""
import pika

# 创建一个连接
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

"""
定义交换机:因为无法确认发布者还是订阅者哪一个先启动
"""
channel.exchange_declare(exchange='logs',exchange_type='fanout')

# 放入消息
channel.basic_publish(exchange='logs',routing_key='',body='Hello World')

connection.close()



