# @Time : 2025/2/27 13:48
# @Author : luoxin

"""
闲置消费：
    只要有消费者闲置，就自动分发给对应的闲置消费者
"""
import pika

# 创建一个连接
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

# 必须在【生产者】声明队列的时候，就定义是否持久化（durable）
channel.queue_declare(queue='hello',durable=True)

# 定义队列持久化，那么message也要持久化,使用properties
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!',
properties=pika.BasicProperties(delivery_mode=2))

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 有闲置消费者立刻消费,每个消费者处理的最大消息量为1
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

