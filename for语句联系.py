# for i in range(0,5):
#     print(i)

for i in range(3):
    username = input("用户名:")
    password = input("密码:")
    if username == 'songsong' and password == '123456' :
        print("欢迎用户:{}".format(username))
        print("-----------轻松购物吧------------")
        break
    else:
        print("输入错误")
else:
    print("账户被锁定，请重新激活")