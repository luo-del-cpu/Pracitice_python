# @Time : 2025/4/2 12:00
# @Author : luoxin
# def test(s):
#     l = []
#     new_l = []
#     for i in s:
#         l.append(i)
#     for _ in range(len(l)):
#         v = l.pop()
#         new_l.append(v)
#     new_s = "".join(new_l)
#     return new_s
#
# s = "abc"
# print(test(s))
import pymysql
from pymysql.constants.ER import PASSWD_LENGTH


# def test1(s):
#     s = list(s)  # 将字符串转换为列表
#     for i, v in enumerate(s):
#         s[i] = s[len(s)-1-i]  # 修改列表中的元素
#     return "".join(s)  # 将列表转换回字符串
#
# s = "abcd"
# print(test1(s))

config = {
    "host": "localhost",
    "USER":"TEST",
    "PASSWD":"TEST",
    "PORT":3306,
    "db":"test"
}

PATH = "./test.text"

def w_mysql(config,PATH):
    with pymysql.connect(**config) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        conn.commit()

    with open(PATH,"r") as f:
        for line in f:
            print(line.strip())

