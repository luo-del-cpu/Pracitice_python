# @Time : 2025/2/27 13:48
# @Author : luoxin


import pika

# 创建一个连接
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

# 声明一个队列，即使生产者已经有队列，但是为了保险起见，消费者也创建；因为无法确认哪个先启动
channel.queue_declare(queue='hello')

# 往队列中放入数据
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

# 定义回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 有消息调用callback函数
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# 开始进行消费
channel.start_consuming()