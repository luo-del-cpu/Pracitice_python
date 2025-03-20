"""
交换机的direct模式：
    在生成者发送消息的时候，需要指明routing_key,便于在交换机绑定队列的时候指定同名的routing_key
    通过这种方式，就可以指定消息发送达到对应的队列了。
"""
import pika

# 创建连接

credentials = pika.PlainCredentials(username='guest', password='<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, credentials=credentials))
channel = connection.channel()

# 定义交换机
channel.exchange_declare(exchange="logs", exchange_type="direct")

# 发送消息并且指定routing_key为error
channel.basic_publish(exchange="logs",routing_key="error",body="Hello World!")

# 关闭连接
channel.close()
connection.close()