# @Time : 2023/11/16 22:45
# @Author : luoxin


# str ---> int、list、set、tuple

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

# int、list、set、tuple、dict、float ---> str

# list ---> set、tuple，可以转成字典，但必须是以下格式[(key,vale),(key,vale),(key,vale)...]

# tuple ---> list    set ---> list   dict ---> lsit(只把key放入列表)
