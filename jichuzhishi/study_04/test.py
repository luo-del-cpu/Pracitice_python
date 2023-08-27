# numbers = [10, 5, 8, 20, 5, 3]
#
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print("存在重复元素:", numbers[i])
#             break
#     else:
#         continue
#     break
# else:
#     print("不存在重复元素")
message = "hello,world"
char = 'i'
found=False
for i,b in enumerate(message):
    #判断是否有相同的字符，如果有，就打印出来
    if b==char:
        print(f"找到了字符{char}，在第{i}的位置")
        #置为true后，就表示有相同的字符
        found = True
    #如果found为false（另外可以证明并没有进入if的判断之内，就没有相同的字符，无法置为true，found依然为false），not found就是true，条件成立，就代表没有找到字符
if not found:
    print("未找到字符")