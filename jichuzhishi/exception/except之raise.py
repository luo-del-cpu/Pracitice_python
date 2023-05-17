# 抛出异常： raise
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')  # 在此处，若是长度小于6位，就会“扔”出去一个错误
    else:
        print('输入的用户名是：', username)


try:
    register()
except  Exception as err:  # 在此处，expect接住raise“扔”出来的错误信息
    print(err)  # 在此处，打印raise“扔”出来的错误信息
    print('注册失败！')
else:
    print('注册成功！')
