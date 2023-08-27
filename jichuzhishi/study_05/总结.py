"""for循环和while循环在以下情况下使用："""

#总之，for循环适用于已知迭代次数的情况，而while循环适用于不确定迭代次数但有条件的情况。

#for循环：
"""
    当你需要对一个可迭代对象（如列表、元组、字符串等）中的每个元素进行迭代时，可以使用for循环。
    它会自动迭代整个序列，并按顺序访问其中的每个元素。
例如：
"""
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
"""
输出：
apple
banana
orange
"""

"""
当你需要对一个指定范围的数值进行迭代时，可以使用range()函数结合for循环。
例如：
"""
for i in range(1, 6):
    print(i)
"""
输出：
1
2
3
4
5
"""

# while循环：

"""
当你需要根据条件重复执行一段代码块时，可以使用while循环。
它会在循环开始前检查一个条件表达式，只要条件为真，就会重复执行循环体，直到条件变为假才会退出循环。
例如：
"""
count = 0
while count < 5:
    print("Hello!")
    count += 1
"""
输出：
Hello!
Hello!
Hello!
Hello!
Hello!
"""

"""
当你不确定循环次数，但知道循环应该在满足某个条件时终止时，可以使用while循环。
例如：
"""
while True:
    answer = input("请输入 'quit' 退出循环：")
    if answer == "quit":
        break
#当用户输入 "quit" 时，循环终止。


