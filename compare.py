# import hashlib
#
#
# def getHash(f):
#     line = f.readline()
#     hash = hashlib.md5()
#     while (line):
#         hash.update(line)
#         line = f.readline()
#     return hash.hexdigest()
#
#
# def IsHashEqual(f1, f2):
#     str1 = getHash(f1)
#     str2 = getHash(f2)
#     return str1 == str2
#
#
# if __name__ == '__main__':
#     f1 = open(r"C:\Users\86176\Desktop\模型匹配测试数据\转\duocipipei\单个规则词\near和after\W1_near_W2\08.json", "rb")
#     f2 = open(r"C:\Users\86176\Desktop\模型匹配测试数据\转\duocipipei\单个规则词\near和after\W1_after_W2\10.json", "rb")
#     p = IsHashEqual(f1,f2)
#     print(p)

import json
f1=open(r"C:\Users\86176\Desktop\模型匹配测试数据\转\duocipipei\单个规则词\near和after\W1_near_W2\08.json", "rb")
f2=open(r"C:\Users\86176\Desktop\模型匹配测试数据\转\duocipipei\单个规则词\near和after\W1_after_W2\10.json","rb")
json1 = json.load(f1)
json2 = json.load(f2)
for json1_list, json2_list in zip(json1, json2):
    if json1_list != json2_list:
        print(json1_list,json2_list)