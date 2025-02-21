# @Time : 2025/2/22 01:58
# @Author : luoxin

"""
旧版本使用gevent
    1.导包 gevent与monkey
    2.打猴子补丁:monkey.patch_all();一定要在导包后打补丁，放的位置越前越好
    3.定义任务函数
    4.生成协程对象:gevent.spawn(函数名，参数)
    5.阻塞主线程，等待协程执行完成:gevent.join(协程对象)
"""
import gevent
from gevent import monkey
# 将阻塞式IO的变为非阻塞式的IO,例如requests，必须将此放在requests之前，否则它可能已经导入了socket等模块导致patch无法正确替换；会出问题
monkey.patch_all()
import requests




def get_response_len(url):
    response = requests.get(url)
    print(f"从{url}下载数据，长度为:{len(response.content)}")

if __name__ == '__main__':
    urls = ["https://www.baidu.com/","https://www.qq.com/","https://www.163.com/"]
    greenlets = [gevent.spawn(get_response_len,url) for url in urls]
    print(greenlets)
    gevent.joinall(greenlets)