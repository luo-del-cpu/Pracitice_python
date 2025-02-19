# @Time : 2023/8/28 23:35
# @Author : luoxin

"""
字符串内建函数：
join(seq):指定字符作为分隔符，将seq中的所有元素(必须是字符串)合并为一个新字符
str.rstrip():去除字符串右侧的空格
str.split():分割字符串后保存到列表中
str.count():求字符串中指定字符的个数
"""

s='abv'
print('-'.join(s))
#输出：a-b-v


"""
1:map(fun,iterable) 用于将一个函数应用到一个或多个可迭代对象的每个元素上，返回一个新的迭代器。
2:可以通过 list() 或其他方法转换为列表。
3：常与 lambda 表达式结合使用，简化代码。

"""
a = [1,2,3,4,5]
print("".join(map(str,a)))
print(list(map(lambda x:x*x,a)))