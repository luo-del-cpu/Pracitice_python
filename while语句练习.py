'''1-20累加计算'''
# sum=0
# i = 1
# while i < 20 :
#     sum += i
#     i+=1
# print('1-20的和：',sum)


'''打印三角形
*
**
***
****
*****
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