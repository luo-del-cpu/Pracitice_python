# @Time : 2025/2/27 13:48
# @Author : luoxin

"""
定义订阅者：
    1：创建连接
    2：定义交换机，exchange_type='fanout'--->将消息发送给所有队列
    3：生成随机的队列
    4：channel.queue_bind交换机与队列绑定
    5：定义回调函数
    6：消费者与队列绑定
    7：启动消费者
"""
import pika

# 创建一个连接
credentials = pika.PlainCredentials('<PASSWORD>', '<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials))
channel = connection.channel()

"""
定义交换机:channel.exchange_declare()
    exchange:交换机名称
    exchange_tye:工作模式（fanout：将消息发送给所有队列）
"""
channel.exchange_declare(exchange='logs',exchange_type='fanout')

# 随机生成一个队列，queue默认为空会随机队列的名称，如果没有明确的名称，那么就是一个临时队列，在消费者关闭连接后，队列会被删除
result = channel.queue_declare(queue='')

# 如果加了exclusive，就表明当前队列只能被当前连接使用，其余的不能使用，同时只能有一个消费者连接占有；
# result = channel.queue_declare(queue='', exclusive=True)

# 让exchange与队列绑定,queue的名字可以使用result.queue_name获取；如果上方起了名字，用起了后的名字就可以
channel.queue_bind(queue=result.queue_name, exchange='logs', routing_key='')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue=result.queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()