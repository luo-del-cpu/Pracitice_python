# @Time : 2025/2/22 00:43
# @Author : luoxin

"""
更加现代的asyncio库
"""

import asyncio
import requests
import aiohttp

async def get_response_len(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # 获取网页内容并打印长度
            print(f"从{url}下载数据，长度为{len(await response.text())}")


async def main():
    urls = ["https://www.baidu.com/","https://www.qq.com/","https://www.163.com/"]
    await asyncio.gather(*[get_response_len(url) for url in urls])


# 运行事件循环
asyncio.run(main())