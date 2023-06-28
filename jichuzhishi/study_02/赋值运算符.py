"""
运算符：
1：赋值运算符
2：算术运算符
3：逻辑运算符
4：位运算符
"""

# 赋值运算符

name = 'admin'
# 将'admin'的值赋值给name

name1 = name
name2 = name
print(id(name), name)
print(id(name1), name1)
print(id(name2), name2)
# id()：可以打印内存地址
"""
4298254192 admin
4298254192 admin
4298254192 admin
其实'admin'相当于开辟了一个内存，name、name1、name2都是从admin这个内存地址中去取的值，这样可以节省内存
"""

"""
扩展后的赋值运算符：+=、-=、*=、/=
+=：可以用于计算与字符串的赋值
其余的赋值运算符不能适用于字符串。只适用于整数类型，只是相当于先做一遍运算在赋值

"""

num = 8
num += 5  # 等效于：num = num+5
print(num)  # 输出13；此时"+"相当于数学中的加号

a = 'ab'
b = 'cd'
a += b  # 等效于：a = a+'cd'
print(a)  # 输出"abcd"，此时"+"相当于连接符号，将a与b两个字符连接起来赋值给a
