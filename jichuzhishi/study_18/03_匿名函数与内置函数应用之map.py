"""
1：map ：map 将传入的函数依次作用到序列的每个元素上., 并把结果作为新的 Iterator 返回，注意返回结果需要转为list
2：lambda 与 map() 一起使用时，通常接收的参数数量与 map() 中可迭代对象的数量一致。
    如果只有一个可迭代对象，lambda 接收一个参数：map(lambda x：x+1,numbers1)
    如果有多个可迭代对象，lambda 会接收多个参数，数量与可迭代对象的数量相同：map(lambda x,y:x+y,numbers1, numbers2)
"""
list_5 = [1, 2, 3, 4, 5, 6, 7, 6]
result = map(lambda x: x * x, list_5)
print(list(result))  # 注意此处需要使用列表转换一下；得出：[1, 4, 9, 16, 25, 36, 49, 36]

#对列表中的奇数进行加1操作
result_1 = map(lambda x:x if x%2==0 else x+1,list_5) #此处注意，在做判断时，
                                                     # 为真的时候将返回的参数x要写在if判断前
print(list(result_1)) #得出：[2, 2, 4, 4, 6, 6, 8, 6]
print(list_5) # [1, 2, 3, 4, 5, 6, 7, 6]

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result)  # 输出: [5, 7, 9]

