# 冒泡排序

numbers = [2, 6, 9, 5, 64, 56, 7, 8, 77]
print("有列表：",numbers)
# 升序排列

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("升序排列：", numbers)

# 降序排列

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("降序排列：", numbers)


#另一种排序方法


for i in range(len(numbers)-1):
    for j in range(len(numbers)-1-i):
        numbers[j] > numbers[j+1]
        numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)
