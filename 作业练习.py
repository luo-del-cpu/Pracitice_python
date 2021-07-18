# s1 = input("请输入第一个字符串：")
# s2 = input("请输入第二个字符串：")
# s3 = ''
# for i in s1:
#     if i not in s2 :
#


# word = input("输入单词：")
# for i in range(len(word)) :
#     if word[i] < 'A' or word[i] > 'Z' :
#         print('不喜欢，不是大写')
#         break
#     else:
#         if i < len(word)-1 and word[i]==word[i+1]:
#             print('不喜欢，有连续相同的字母')
#             break
# else:
#     print('喜欢')

s1 = ''
while True:
    username = input('输入用户名：')
    password = input('输入密码：')
    email = input('输入邮箱：')

    username = username[0:20]
    password = password[0:20]
    email = email[0:20]

    msg = '{}\t{}\t{}\n'.format(username,password,email)

    msg = msg.expandtabs(20)

    s1+=msg

    if username == 'q' or username == 'Q' or password =='q' or password=='Q' or email =='q' or email =='Q':
        break
print(s1)

