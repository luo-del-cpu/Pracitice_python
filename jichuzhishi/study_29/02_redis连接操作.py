# @Time : 2024/7/10 23:19
# @Author : luoxin

import redis

def main():
    client = redis.Redis(host='',port='',password='')

    #直接调用redis的操作方法就行
    client.set()

if __name__ == '__main__':
    main()