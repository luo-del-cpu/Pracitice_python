''''
递归函数：函数自己调用自己
1.普通函数的一种表现形式

特点：
1.必须要设定一个终点
2.通常都会有一个入口

'''

def sum(n): #求一个1~n的和
    if n ==0: # 当递归函数执行到终点时，在else里的递归就会一层一层的向上return回最上层进行累加操作
        return 0
    else:
        return n+sum(n-1)
result = sum(10)
print(result) #55