# @Time : 2025/2/27 13:48
# @Author : luoxin

"""
ack回复：
    为什么需要ack回复？
        如果消费者把消息拿走了，但是没有回复；队列就会重新再生成一条消息；
        如果消费者回复，那么就会清除这条消息
"""
import pika

# 创建一个连接
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # 消息处理完毕后发送 ACK，确认已处理该消息
    ch.basic_ack(delivery_tag=method.delivery_tag)

# auto_ack默认关闭为true，不需要消息确认；如果是false，就需要手动调用，如回调函数找那个的ch.basic_ack
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

