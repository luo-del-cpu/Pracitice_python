# @Time : 2025/5/22 23:14
# @Author : luoxin

"""
判断一个是是否是回文
"""
def test(s):
    left,right=0,len(s)-1
    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True


s = "cba"
print(test(s))

"""
反转字符串
"""
def test1(s):
    l = list(s)
    left,right=0,len(s)-1
    while left<right:
        l[left],l[right] = l[right],l[left]
        left+=1
        right-=1
    return "".join(l)

s1 = "cba"
print(test1(s1))

def test2(s):
    l = list(s)
    l1 = []
    for i in range(len(l)):
        l1.append(l.pop())
    return "".join(l1)

s = "abc"
print(test2(s))

"""
计算数组中除自己以外的乘积
"""

l = [1,2,3,4]
new_l = [24, 12, 8, 6]


def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    # 左积
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    # 右积
    right = 1
    for i in reversed(range(n)):
        res[i] *= right
        right *= nums[i]

    return res

print(product_except_self([2,2,3,4]))

def test3(s):
    n = len(s)
    res = [1]*n

    left = 1
    for i in range(n):
        res[i] = left
        left *= s[i]

    right = 1
    for i in reversed(range(n)):
        res[i] *= right
        right *= s[i]
    return res


print(test3([2, 2, 3, 4]))


"""找出出现两次的数字"""

from collections import Counter

def test4(s):
    d = Counter(s)
    l = []
    for k,v in d.items():
        if v > 1:
            l.append(k)
    return l

print(test4("aacbb"))


a= Counter("aabbcc")
for k in a:
    print(k)
    print(a[k])