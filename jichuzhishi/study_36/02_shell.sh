#!/bin/bash

# 脚本功能：接收用户输入的参数进行计算

#定义函数，打印错误提示语
print_error() {
    echo "Error: 输入必须是数字"
    exit 1
}
#接收用户输入的第一个参数
read -p "请输入第一个整数：" num1

#判断输入是否为整数
#if ! [[ $num1 =~ ^[0-9]+$ ]]; then # 两个[[]]可以使用正则匹配
#    print_error # 调用函数
#fi

if [ -n "`echo $num1 | sed 's/[0-9]//g'`" ] # -n对字符串判断，为空，不成立；不为空，成立；
then
    print_error
fi

# 接收用户输入的第二个参数
read -p "请输入第二个整数：" num2

# 判断输入是否为整数
if [ -n "`echo $num2 | sed 's/[0-9]//g'`" ] # [ -n ]判断不为空成立，执行then语句
then
    print_error
fi

# 接收用户输入的运算符
read -p "请输入运算符(+|-|*|/)：" operator
# 判断输入的运算符是否有效
#case $operator in
#    +)
#        ;;
#    -)
#        ;;
#    *)
#        echo "Error: 输入的运算符无效"
#        exit 1
#        ;;
#esac

if [ "$operator" != "+" ] && [ "$operator" != "-" ] && [ "$operator" != "*" ] && [ "$operator" != "/" ]
then
    echo "Error: 输入的运算符无效"
    exit 2
fi

# 进行运算并打印结果
echo "${num1}${operator}${num2}=$((${num1}${operator}${num2}))"