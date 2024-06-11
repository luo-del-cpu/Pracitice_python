# @Time : 2023/11/14 22:45
# @Author : luoxin


"""
set:集合
特点：无序不重复的
声明方式：
1:s1=set():创建空集合，只能使用set()
2:s2={元素1,元素2,...}
"""

"""
新增：
s1.add():添加一个元素
s1.update():添加多个元素
"""

s1 = set()
s1.add('hello')
s1.add('测试')
print(s1)  # {'hello', '测试'}

t1 = ('新增1', '新增2')
s1.update(t1)
print(s1)  # {'测试', '新增1', '新增2', 'hello'}

"""
删除：
s1.remove():删除一个元素，如果不存在，则报错
s1.pop():随机删除，但是一般都是删除第一个
s1.clear():清空集合
s1.discard():如果要删除的值不存在，不会报错
"""
s1.remove('测试')
print(s1)  # {'新增2', '新增1', 'hello'}
s1.remove('不存在')  # KeyError: '不存在'
