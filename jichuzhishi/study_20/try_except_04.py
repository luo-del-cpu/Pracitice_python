# @Time : 2024/6/5 21:53
# @Author : luoxin

# 抛出异常 raise

# 用户注册 名称必须在6位以上

def register():
    username = input("输入用户名：")
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')  # 一般这里需要自己定义类，然后继承Exception，将异常抛出去
    else:
        print("输入的用户名是", username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')
