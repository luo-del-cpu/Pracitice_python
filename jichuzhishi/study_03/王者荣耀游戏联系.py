# 游戏：
'''
1:选择人物
2：购买武器  金币
3：打仗 赢   金币
4：删除武器
5：退出游戏
'''

import random
from numpy import *



print("*" * 50)
print("\t欢迎来到王者荣耀")
print("*" * 50)

role = input("请选择你的人物：1.鲁班 2.后裔 3.孙尚香 4.刘备 5.虞姬")
coins = 1000
my_weapon_list = []


print("欢迎{}进入游戏！！！您的金币：{}".format(role, coins))

while True:
    choice = int(input("请选择：\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n"))
    if choice == 1:
        # 购买武器功能
        print("欢迎进入武器库！！！")
        weapons = [['电刀', 500], ['无尽', 1000], ['战斧', 1200], ['帽子', 2000]]
        for weapon in weapons:
            print(weapon[0], weapon[1], sep='    ')
        # 提示输入购买的武器
        weaponname = input("请输入要购买的武器名称：")
        # 1.原来有没有买过武器 2.输入的武器名是否在武器库
        if weaponname not in my_weapon_list:
            # 输入的武器名是否在武器库
            for weapon in weapons:
                if weaponname in weapon[0]:
                    # 购买武器
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        my_weapon_list.append(weapon[0])
                        print("{}购买{}成功；当前剩余金币：{}".format(role, weaponname, coins))
                        break
                    else:
                        print("金币不足")
                        break
            else:
                print("输入的武器名称错误！")
        else:
            print("你的武器库中已经存在该武器，无需重复购买！！！")
    elif choice == 2:
        # 打仗 假设有多个武器
        print("进入战场。。。")
        if len(my_weapon_list) > 0:
            # 选择武器
            print("{}拥有的武器如下：".format(role))
            for weapon in my_weapon_list:
                print(weapon)
            while True:
                weaponname = input("请选择你的武器进行战斗：")
                if weaponname in my_weapon_list:
                    # 进入战场成功,默认与张飞对战（用数字比大小决出胜负）
                    print("开始战斗。。。")
                    ran1 = random.randint(1, 20)  # 张飞
                    ran2 = random.randint(1, 20)  # role
                    print("张飞生成的数字{}；{}生成的数字：{}".format(ran1, role, ran2))
                    if ran1 > ran2:
                        print("张飞胜")
                    else:
                        coins += 200
                        print("{}胜利，当前金币：{}".format(role, coins))
                    break
                else:
                    print("选择的武器不存在，请重新选择！！！")
        else:
            print("请先购买武器！！！！")
    elif choice == 3:
        # 删除武器
        if len(my_weapon_list) > 0:
            print("武器太多，扔掉几个。。。")
            print("{}拥有的武器如下：".format(role))
            for weapon in my_weapon_list:
                print(weapon)
            while True:
                weaponname = input("输入要删除的武器名称：")
                if weaponname in my_weapon_list:
                    # 删除武器
                    my_weapon_list.remove(weaponname)
                    # 将删除的武器的钱退回给账户
                    print(weapons[0],weapons[1],type(weapons[0]),type(weapons[1]))
                    for weapon in weapons:
                        if weaponname == weapon[0]:
                            coins += len(weapons[1])
                            break
                    print("剩余金币：{}".format(coins))
                    break
                else:
                    print("武器名称输入有误！")
                    print("当前武器库剩余武器：", my_weapon_list)
        else:
            print("没有需要删除武器")
    elif choice == 4:
        print("{}拥有的武器如下：".format(role))
        for weapon in my_weapon_list:
            print(weapon)
    elif choice == 5:
        answer = input("确定要退出游戏吗？（yes/no）")
        if answer == "yes":
            break
        else:
            print("输入错误！！！请重新输入")
