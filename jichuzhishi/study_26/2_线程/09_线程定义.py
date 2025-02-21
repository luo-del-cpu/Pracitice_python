# @Time : 2025/2/21 19:02
# @Author : luoxin
"""
线程
    比进程还小的单元，但是基本与进程创建的方式相同
    1.创建
        t1 = threading.Thread(target=download,name='download',args=(1,))
        t1.start()
    2.状态
        新建-->就绪-->运行-->阻塞-->结束；
        注意：阻塞完成之后要去就绪状态
"""
from time import sleep
import threading

def download(n):
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    for image in images:
        print('downloading', image)
        sleep(n)
        print(f'下载{image}成功')

def listen_music():
    songs = ["北京欢迎你","放生","爱无罪"]
    for song in songs:
        sleep(0.5)
        print(f"正在听{song}")

if __name__ == '__main__':
    # 创建线程对象
    t1 = threading.Thread(target=download,name='download',args=(1,))
    t1.start()

    t2 = threading.Thread(target=listen_music,name='listen_music')
    t2.start()
