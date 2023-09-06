# @Time : 2023/9/6 23:08
# @Author : luoxin


"""
王者荣耀：
1：选择人物
2：购买武器、金币
3：打仗、赢 得金币
4：选择删除武器
5：查看武器
6：退出游戏
"""
import random

print('*' * 50)
print('\t\t\t\t欢迎来到王者荣耀')
print('*' * 50)

role = input('请选择游戏人物：1：李白；2：貂蝉；3：鲁班 \n')
coins = 1000
weapon_list = []
print('-' * 50)
print(f'欢迎{role}进入游戏,金币余额{coins}')
print('-' * 50)

while True:
    choice = int(input('请选择：\n 1；购买武器\n 2: 打仗\n 3：删除武器\n 4：查看武器\n 5: 退出游戏\n'))
    if choice == 1:
        # 购买武器
        print('欢迎进到武器库:')
        weapons = [['刀', 100], ['枪', 500], ['棍', 1000], ['棒', 1200]]
        # 查看武器
        for weapon in weapons:
            print(weapon[0], weapon[1], sep='   ')

        # 提示输入购买的武器
        weaponname = input('请输入要购买的武器名称:')

        # 1:原来有没有购买过武器 2:输入的武器名是否在自己的武器库
        # 输入的武器名是否在武器库
        if weaponname not in weapon_list:
            for weapon in weapons:
                if weaponname == weapon[0]:
                    # 购买武器
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        weapon_list.append(weapon[0])  # 添加到自己的武器库
                        print(f'{role}购买{weaponname}成功')
                        break
                    else:
                        print('金币不足！！！')
                        break
            else:
                print('输入名称有误！！！')
        else:
            print('已经拥有此武器！！！')
    elif choice == 2:
        # 打仗
        print('进入战场。。。。')
        if len(weapon_list) > 0:
            # 选择武器
            print(f'{role}拥有的武器如下:')
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('选择你的武器:')
                if weaponname in weapon_list:
                    # 进入决斗
                    ran1 = random.randint(1, 20)
                    ran2 = random.randint(1, 20)
                    if ran1 > ran2:
                        print('npc胜')
                    elif ran1 < ran2:
                        coins += 200
                        print(f'{role}胜，金币{coins}')
                    else:
                        print('平局')
                    break
                else:
                    print('输入有误，请重新输入')
        else:
            print('请先购买武器！！！')
    elif choice == 3:
        # 删除武器
        print('武器太多，需要删除。。。')
        if len(weapon_list) > 0:
            print(f'{role}拥有的武器如下:')
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('请选择武器删除的名称:')
                if weaponname in weapon_list:
                    # 删除武器
                    weapon_list.remove(weaponname)
                    print(f'---删除{weaponname}成功---')
                    # 删除后返回金币
                    for weapon in weapons:
                        if weaponname == weapon[0]:
                            coins += weapon[1]
                            break
                    break
                else:
                    print('输入有误，重新输入')
        else:
            print('没有武器！！！')
    elif choice == 4:
        # 查看武器
        print(f'{role}拥有的武器如下:')
        for weapon in weapon_list:
            print(weapon)
        print(f'总金币{coins}')
    elif choice == 5:
        answer = input('确认离开游戏么？y/n')
        if answer == 'y':
            print('退出游戏！！！')
            break
    else:
        print('输入有误，请重新选择！！！')
