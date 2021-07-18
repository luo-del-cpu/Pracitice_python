'''
map ：map 将传入的函数依次作用到序列的每个元素上., 并把结果作为新的 Iterator 返回，注意返回结果需要转为list
map(lambda x,y:x+y,可迭代的数据)
'''
list_5 = [1, 2, 3, 4, 5, 6, 7, 6]
result = map(lambda x: x * x, list_5)
print(list(result))  # 注意此处需要使用列表转换一下；得出：[1, 4, 9, 16, 25, 36, 49, 36]

#对列表中的奇数进行加1操作
result_1 = map(lambda x:x if x%2==0 else x+1,list_5) #此处注意，在做判断时，
                                                     # 为真的时候将返回的参数x要写在if判断前
print(list(result_1)) #得出：[2, 2, 4, 4, 6, 6, 8, 6]
print(list_5)