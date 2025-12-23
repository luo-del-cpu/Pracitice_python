# @Time : 2023/11/16 22:45
# @Author : luoxin
from jichuzhishi.study_07.list_demo1 import names

# str ---> int、list、set、tuple：除转换成int外，其余的都是将字符串拆开放入对应的容器

s = '8'
i = int(s)
print(i)

s = 'abc'
l = list(s)
print(l)  # ['a', 'b', 'c']

s = 'def'
t = set(s)
print(t)  # {'f', 'e', 'd'}

t = tuple(s)
print(t)  # ('d', 'e', 'f')


# int、list、set、tuple、dict、float ---> str：在最外层包裹一个引号
print(type("[1,2,3]"))
print(type("{1,2,3}"))
print(type("(1,2,3)"))
print(type("{'name':'jck','age':'18'}"))
print(type("1.2"))

# list ---> set、tuple，dict(可以转成字典，但必须是以下格式[(key,vale),(key,vale),(key,vale)...])
print(f"list-->set:{set([1,3,2,3,2])}")  # 等价于 {1,2,3}
print(f"list-->tuple:{tuple([1,3,2,3,2])}") # (1, 2, 3)
print(dict([('name','jck'),('age','18')])) # {'name': 'jck', 'age': '18'}

# tuple ---> list
print(list((1,2,3))) # [1, 2, 3]

# set ---> list
print(list({1,2,3})) # [1,2,3]

#dict ---> list(只把key放入列表)

print(list({'name': 'jck', 'age': '18'})) # ['name','age']

