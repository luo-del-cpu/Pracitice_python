"""
结构：
for 变量名 in 集合：
    语句
"""

"""
for i in 集合：
    有数据执行的语句
else：
    没有数据执行的数据
    
pass 空语句，用于占位避免语法错误
"""

'''
break语句：
跳出整个循环结构，结束循环；继续执行for循环下方的语句

for...else...
else：1：适用于for执行完或者没有循环数据时，需要做的事情；2：必须是for循环正常执行完成才会执行，如果因为
break跳出了循环，那么else也不会执行

例如：用户登录页面，如果3次输入错误，那么账户就被锁定
'''
# for i in range(3):
#     username=input("输入用户名:")
#     password=input("输入密码:")
#     if username =='luoxin' and password=='123456':
#         print("登录成功")
#         print("---轻松购物---")
#         break
#     else:
#         print('用户名或密码错误')
# else:
#     print("账户锁定")

for i in range(3):
    if i==1:
        print('毒馒头')
        break
    else:
        print("馒头真香")
print("投诉你")

"""
contiue语句：
用于在循环结构中跳过当前迭代并开始下一次迭代。
当程序执行到continue语句时，它会立即停止当前迭代的执行，并且会忽略后续代码，直接回到循环的顶部开始下一次迭代。

continue通常与条件语句结合使用，以便根据特定条件跳过循环的一部分代码。
如果条件满足，continue语句将被执行，否则将继续执行循环体中的其余代码。

注意：
1:continue语句只能在循环结构（如for循环、while循环）中使用，而不能用于其他地方。
2:此外，continue语句只会影响到当前所在的循环体，如果存在嵌套循环，continue语句只会跳过当前内层循环的代码，
并开始下一次迭代。
"""

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
"""
输出：
1
2
4
5
"""