"""
交换机的topic模式：
    定义交换机的模式为topic
    在发消息的时候执行routing_key关键字参数
"""
import pika

# 创建连接

credentials = pika.PlainCredentials(username='guest', password='<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, credentials=credentials))
channel = connection.channel()

# 定义交换机为topic模式
channel.exchange_declare(exchange="logs", exchange_type="topic")

# 发送消息并且指定routing_key
channel.basic_publish(exchange="logs",routing_key="animals.dog",body="Hello World!")

# 关闭连接
channel.close()
connection.close()