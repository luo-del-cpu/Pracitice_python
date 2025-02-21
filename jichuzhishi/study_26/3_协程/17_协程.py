# @Time : 2025/2/22 00:43
# @Author : luoxin

"""
协程:
    定义：
        是一种 轻量级的线程，它允许程序在某个点暂停执行并将控制权交还给其他任务（如 I/O 操作、其他计算任务等），然后再从暂停的位置继续执行。
        这使得程序能够在等待 I/O 操作时执行其他任务，最大限度地利用 CPU 时间，因此 协程特别适用于 I/O 密集型任务。
        与线程相比，协程更轻量，因为它们通常由程序员手动控制，不依赖操作系统的调度，因此协程比线程的创建和销毁更加高效。
    使用：
        更加现代的asyncio库。
            1.async：定义一个协程函数。
                async def task():
                    ...
                2.await：在协程中暂停执行，等待异步操作的完成，然后恢复执行。
            3.async def main(): 定义异步入口
                await asyncio.gather(task())
            4.asyncio.run(main()) 启动事件函数
"""

import asyncio

async def task1():
    print("task1开始")
    await asyncio.sleep(2)
    print("task1结束")

async def task2():
    print("task2开始")
    await asyncio.sleep(1)
    print("task2结束")

async def task3():
    print("task2开始")
    await asyncio.sleep(1)
    print("task3结束")

# async def main() 是程序的入口
async def main():
    # 使用 gather() 进行任务并发执行
    await asyncio.gather(task1(), task2(), task3())

# # 启动事件循环并执行 main 函数
asyncio.run(main())