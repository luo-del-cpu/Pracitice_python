# dict1 = {}
# dict1['brand']='huawei'
# print(dict1)

'''
案例：用户注册
username
password
email
phone
...
'''

print("欢迎注册")

#模拟一个数据库用来存放用户信息
# database = []
#
# while True:
#     username = input("输入用户名：")
#     password = input("输入密码：")
#     repassword = input("确认密码：")
#     email = input("输入邮箱：")
#     phone = input("输入电话号码：")
#
#     #定义一个字典
#     user = {}
#
#     #将信息保存到字典中
#     user['username'] = username
#     if repassword == password:
#         user['password'] = password
#     else:
#         print("两次密码不一致!!!")
#         continue
#     user['email'] = email
#     user['phone'] = phone
#
#     database.append(user)
#
#     answer =input("是否继续注册？（yes/no）")
#
#     if answer != 'yes':
#         break
# print(database)

dict1 = {'张三':100,'李四':80,'王五':90}
dict2 = {'张三':10,'赵四四':70,'王五':100}
result =dict1.update(dict2)
# print(result)
# print(dict1)
print(dict1.pop("李四"))
# print(dict1.pop())
# print(dict1)

# print(dict1.get('赵四',99))
# print(dict1)
#
# print('张三' in dict1)
# print(100 in dict1)
#
# print(dict1.items())
# print(dict1.values())
# print(dict1.keys())