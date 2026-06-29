# LeetCode 53 — Maximum Subarray

# Given an integer array nums, find the contiguous subarray with the largest sum and return that sum.
# Example: nums = [-2,1,-3,4,-1,2,1,-5,4] → answer is 6 (from subarray [4,-1,2,1]).


### Thoughts
# 历遍整个数组（for num in nums），keep track of max_sum和子数组的和（加上num） 
# 每一步更新最大和

### TC:O(n) - n in len(nums)
### SC:O(1) - update variables

### Kadane's algorithm. 
# The idea: as you scan left to right, track the best sum of a subarray ending at the current position (num). 
# At each element you decide whether to extend the previous subarray or start fresh from the current element (num) — whichever is larger.

### Why this is DP?
# 每一步都基于前一步的最优解，只依赖前一步结果
# 状态转移方程：cum_sum = max(num, cum_sum + num) # state transfer fomula
# 每一步都在做局部最优，最终得到全局最优
      
def maxSubArray(nums: list[int]) -> int:
    max_sum = cum_sum = nums[0]
    
    for num in nums[1:]:
        # cum sum = 当前元素/当前元素+之前的和,whichever largest
        # If the running sum cur has gone negative, it can only drag down whatever comes next, so you drop it and restart at x
        cum_sum = max(num, cum_sum + num) # state transfer fomula
        max_sum = max(max_sum, cum_sum)
    return max_sum


### divide and conquer - O(nlogn)
# 核心观察：把数组从中点 mid 切成左右两半后，最大子数组只可能落在三种情况之一：

# 完全在左半部分
# 完全在右半部分
# 横跨中点（必须同时包含 mid 和 mid+1）

# 前两种情况递归解决。第三种是分治的关键——它不能简单递归，必须单独算，因为它必须跨越分割线，子问题里不会出现。
# 怎么算跨中点的最大和？ 既然必须包含中点，就从 mid 向左扩展，求"以 mid 为右端点、向左能取到的最大和"；再从 mid+1 向右扩展，求"以 mid+1 为左端点、向右能取到的最大和"。两者相加就是跨中点的最优解。这一步是线性扫描。
# 最终答案 = 三者取最大。

### TC - O(nlogn)
# T(n) = 2·T(n/2) + O(n)
    #     ↑          ↑
    #  左右两半递归   两个for循环扫整段

# 为什么一共 log n 层
# 因为每往下递归一层，区间长度就对半砍一次，而砍到长度为 1 时就停（left == right 的 base case）。"一个数能被对半除多少次才到 1"——这个次数就是 log₂n。
# 一步步看，从长度 n 开始：
# n → n/2 → n/4 → n/8 → … → 1
# 每个箭头代表下沉一层。要问经过多少个箭头到 1，就是解这个方程：
# n / 2^k = 1   →   2^k = n   →   k = log₂ n
# 所以层数 k = log₂ n。
# 直觉验证：n = 8 时，8 → 4 → 2 → 1，3 次对折，而 log₂8 = 3，对上了。n = 1024 时，对折 10 次到 1，log₂1024 = 10。每翻一倍，只多一层——这正是 log 增长慢的体现。

### SC - O（logn）- 全部来自递归，中点部分计算全部都是variables所以只有O（1）
# 栈的最大高度 = 递归树的高度 = 这条最长路径的长度，正好就是上一条消息里推出来的 log n 层。因此栈空间是 O(log n)。

def helper(nums, left, right): # left and right are array indexes
    if left == right: # only one element in nums
        return nums[left]
    
    mid = (left + right) // 2

    # recursion on left half and right half
    # 递归(那两句)负责"完全在左"和"完全在右"——这两种和原问题同构,可以放心交给递归。
    left_max = helper(nums, left, mid)
    right_max = helper(nums, mid + 1, right)

    # for 循环(mid 部分)负责"横跨中点"：这种递归覆盖不到,必须单独线性处理。
    # if the best subarray overlaps with mid
    # 从mid向左推，找到最大值left_sum
    left_sum = nums[mid]
    cum_sum = 0

    for i in range(mid, left - 1, -1):
        cum_sum += nums[i] 
        left_sum = max(left_sum, cum_sum)

    # 从mid向右推，找到最大值right_sum
    right_sum = nums[mid]
    cum_sum = 0

    for i in range(mid, right + 1):
        cum_sum += nums[i] 
        right_sum = max(right_sum, cum_sum)

    # return the max of three sums
    return max(left_max, right_max, left_sum + right_sum)


def maxSubArray(nums: list[int]) -> int:
    return helper(nums, 0, len(nums))




