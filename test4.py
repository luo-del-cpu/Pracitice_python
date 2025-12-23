# @Time : 2025/3/31 16:36
# @Author : luoxin

"""
阶乘
"""
def test(n):
    if n == 0:
        return 1
    return n * test(n - 1)

print(test(5))

"""
二分法查找目标值；有序
"""

def fing_target(nums, target):
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            left =mid +1
        elif nums[mid] > target:
            right = mid -1
    return -1

nums = [1,2,3,4,5,6,7,8,9]
print("--->",fing_target(nums,8))

"""
二分查找最小值，旋转数组
"""

def fing_target1(nums):
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right)//2
        if nums[mid] > nums[right]:
            left =mid +1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right-=1
    return nums[left]

nums = [5,6,7,8,9,1,2,3,4]
print("--->",fing_target1(nums))

"""
找出重复的数字
"""
from  collections import Counter
def find_duli(nums):
    d = Counter(nums)
    l = []
    for k,v in d.items():
        if v > 1:
            l.append(k)
    return l

nums = [1,2,3,3,2]
print(find_duli(nums))

def find_duli2(nums):
    d = {}
    l= []
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
    for k,v in d.items():
        if v > 1:
            l.append(k)
    return l
nums = [1,2,3,3,2]
print(find_duli2(nums))


"""
找出重复的元素并且输出他们的位置
"""
def find_duli2(nums):
    d = {}
    d_l= {}
    l= []
    for i,v in enumerate(nums):
        if v in d:
            d[v]+=1
            d_l[v].append(i)
        else:
            d[v]=1
            d_l[v]=[i]
    for k,v in d.items():
        if v > 1:
            l.append((k,d_l[k]))
    return l
nums = [1,2,3,3,2]
print("#####",find_duli2(nums))

"""
斐波那契数列
"""

def fibonacci_recursive(n):
    if n<=1:
        return n;
    a,b = 0,1
    for i in range(2,n+1):
        a,b = b,a+b
    return b
print(fibonacci_recursive(10))

"""
计算数组中相加的两个数的和与目标值相同的索引
"""

def find_index(nums,target):
    d = {}
    for i,v in enumerate(nums):
        com = target-v
        if com in d:
            return [d[com],i]
        d[v]=i
    return None
nums = [1,2,3,3,2]
target = 5
print(find_index(nums,target))

"""
冒泡排序
"""

def mao_pao(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
nums = [1,2,3,3,2]
mao_pao(nums)
print(nums)

"""
快速排序：
"""

def quick_sort(arr):
    # print(f"当前数组: {arr}")  # 输出当前递归处理的数组
    if len(arr) <= 1:
        return arr  # 递归出口：长度为0或1的数组已经有序
    pivot = arr[0]  # 选第一个元素作为基准值
    left = [x for x in arr[1:] if x <= pivot]  # 小于等于 pivot 的放左边
    right = [x for x in arr[1:] if x > pivot]  # 大于 pivot 的放右边
    # print(f"基准值: {pivot}, 左边: {left}, 右边: {right}")  # 输出基准值和左右部分
    return quick_sort(right) + [pivot] + quick_sort(left)  # 递归排序并拼接结果

# 示例
arr = [3, 6, 1, 5, 2, 4]
sorted_arr = quick_sort(arr)
print(f"排序结果: {sorted_arr}")

"""
二叉树的前序遍历,非递归
"""
# 定义二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def er_cha_shu(self,root:TreeNode):
        result = []
        if not root:
            return None
        s = [root]
        while s:
            node = s[-1]
            s.pop()
            result.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
a = Solution()
print(a.er_cha_shu(root))

"""
二叉树的前序遍历,递归
"""

class Solution1:
    def er_cha_shu1(self,root:TreeNode):
        pass


class Solution:
    def FindNumsAppearOnce(self, nums: List[int]) -> List[int]:
        # write code here
        d = {}
        l = []
        for i in nums:
            if nums in d:
                d[nums] += 1
            else:
                d[nums] = 1
        for k, v in d.items():
            if v == 1:
                l.append(k)
        return l
