"""
进程间的通信通过队列（queue）来进行通信
    步骤：
        1.创建q队列
        2.通过进程将参数传递给函数
        3.函数持有相同的q
        4.函数中使用q进行通信
"""

from multiprocessing import Queue, Process
from time import sleep

# 每个任务都拿到相同的q
def download(q):
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    for image in images:
        print('downloading', image)
        sleep(1)
        q.put(image)



def getprofile(q):
    while True:
        try:
            # 5s超时过后取不到就报错，进入except
            file = q.get(timeout=5)
            print(f'{file}保存成功')
        except:
            print("全部保存成功")
            break

if __name__ == '__main__':
    # 创建队列用于通信
    q = Queue(5)
    # 将队列传递给任务
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getprofile,args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('done')