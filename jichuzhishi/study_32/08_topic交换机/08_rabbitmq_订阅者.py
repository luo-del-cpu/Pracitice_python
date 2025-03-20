"""
交换机的topic模式：
    其余内容都与direct交换机模式没有区别，除了类型定义为topic外。
    还需要再绑定交换机时指定routing_key的匹配模式。
    例如：
        使用animails.*:代表匹配animails.开头，后续只能跟一个单词的消息
        使用animails.#:代表匹配animails.开头，后续可以匹配0个或多个单词的消息
        使用animails.*.small:代表匹配animails.开头，中间只能匹配一个单词，后续以small结尾的消息
"""
import pika

# 创建连接

credentials = pika.PlainCredentials(username='guest', password='<PASSWORD>')
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, credentials=credentials))
channel = connection.channel()

# 定义交换机
channel.exchange_declare(exchange="logs", exchange_type="topic")

# 定义队列
result = channel.queue_declare(queue='')

# 交换机与队列绑定清切指定routing_key
channel.queue_bind(queue=result.queue_name, exchange="logs",routing_key="animals.*")

# 定义回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 开始消费消息
channel.basic_consume(queue=result.queue_name, on_message_callback=callback, auto_ack=True)

# 启动消费
channel.start_consuming()