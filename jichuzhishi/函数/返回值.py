# 返回值：将函数中运算的结果通过return关键字扔出来
def add(a,b):
    result=a+b
    # print(result)
    return 'aaa',11,result#扔出多个用一个参数接就会将参数放在元组中
x=add(2,5)
print(x) #('aaa', 11, 7)

'''
return 返回值
1.return后面可以是一个参数，接受的时候使用一个变量(x=add(2,5))去接
2.return后面也可以是多个参数，如果是过个参数则底层会将多个参数先放在一个元组中
  将元组作为整体返回   x=add(2,5)
3.接收的时候也可以是多个：return ’hello‘,'word'  x，y=('hello','word')--->x='hello' y='word'
'''
