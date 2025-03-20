#!/bin/bash


# echo：-n:不换行输出；-e:支持转义字符；
#echo "Hello, World!"
#echo -n "Hello, World!" # 输出Hello, World!test...
#echo -e "test, \nWorld!" # 不加-e，输出test, \nWorld!

for file in *finish*.jpg;
do
    mv "$file" "${file//_finished/}"
done