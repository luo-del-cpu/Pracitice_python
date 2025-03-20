"""
交换机的direct模式：
    1：定义交换机的时候：exchange_type="direct"
    2：交换机与队列绑定指定routing_key，注意与发送消息的时候的routing_key要一致
"""
import pika

# 创建连接

credentials = pika.PlainCredentials(username='guest', password='<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, credentials=credentials))
channel = connection.channel()

# 定义交换机
channel.exchange_declare(exchange="logs", exchange_type="direct")

# 定义队列
result = channel.queue_declare(queue='')

# 交换机与队列绑定指定routing_key，注意与发送消息的时候的routing_key要一致
channel.queue_bind(queue=result.queue_name, exchange="logs",routing_key="error")

# 定义回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 开始消费消息
channel.basic_consume(queue=result.queue_name, on_message_callback=callback, auto_ack=True)

# 启动消费
channel.start_consuming()