# @Time : 2024/6/20 20:39
# @Author : luoxin
import re

"""
.（点）：匹配除了换行符之外的任何单个字符。
\d：等价于 [0-9]，匹配数字。
\D：匹配非数字字符。
\w：匹配任何单词字符（等价于 [a-zA-Z0-9_]）。
\W：匹配任何非单词字符。
\s：匹配任何空白字符（包括空格、制表符、换页符等）。
\S：匹配任何非空白字符。
[^abc]：匹配任何不在方括号中的字符。
\b：匹配一个单词边界，即字与空格间的位置。
\B：非单词边界匹配。
"""

msg_1 = 'aa.py uu.txt bb.py cc.png'
# 找出“py”结尾的

# 一般使用缩写需要使用r表示不转译
# \. 表示普通的点，而不是正则里的点匹配任何
# 一般空格就代表边界
print(re.findall(r'\w+\.py\b', msg_1))
