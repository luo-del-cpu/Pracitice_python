"""
while用法结构：

while 条件：
    循环执行的代码

解释一下这个语法：
    "条件" 是一个布尔表达式，当条件为真时，循环会一直执行。
    冒号 ":" 用来表示代码块的开始。
    在冒号下面缩进的代码块是循环体，会重复执行直到条件不满足。
"""

'''1-20累加计算'''
# sum=0
# i = 1
# while i < 20 :
#     sum += i
#     i+=1
# print('1-20的和：',sum)


'''打印三角形
*          第一层1颗星
**         第二层2颗星
***        第三层3颗星
****       第四层4颗星
*****      第五层5颗星
嵌套循环
'''
# ceng = 1
# while ceng <=5 :
#     count = 1
#     while count<=ceng:
#         print('*',end='')
#         count+=1
#     print()
#     ceng+=1

'''九九乘法表'''
# ceng = 1
# while ceng <= 9 :
#     count = 1
#     while count <= ceng :
#         print("{}*{}={}  ".format(count,ceng,count*ceng),end='')
#         count+=1
#     print()
#     ceng+=1

'''掷骰子游戏'''
import random
print('*' * 30)
print("欢迎进入游戏")
print('*' * 30)

username = input("请输入用户名：")
money = 0
answer = input("确定进入游戏么(y/n)?")

if answer =='y':

    while money < 2 :
        n = int(input("金币不足，请充值(100块钱30个币，充值必须是100的倍数:"))
        if n%100==0 and n >0:
            money=(n//100)*30
    print("当前金币剩余：{},玩一局游戏扣除2个币".format(money))
    print("进入游戏。。。。。。。。。。。")
    while True:
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)
        money-=2
        print("洗牌结束，开始猜大小：")
        guess = input("输入大或小")
        if (t1+t2)>6 and guess == "大" or (t1+t2<=6 and guess =="小"):
            print("恭喜{}，本局获得一个游戏币".format(username))
            money+=1
        else:
            print("很遗憾，你输了")

        answer_1 = input("是否继续游戏，继续游戏将扣除2个游戏币(y/n)")
        if answer_1 != "y" or money < 2:
            print("退出游戏！！！")
        break
    print("当前剩余金币：",money)