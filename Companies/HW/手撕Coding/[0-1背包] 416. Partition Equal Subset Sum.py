# 416. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or false otherwise.
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

### Thoughts
# 0/1背包，加到sum/2
# 求 total = sum(nums)——先想一个 early return:什么情况下直接返回 False?
# target = total // 2
# dp[x] = 能否用某个子集恰好凑出 x, so full of 1 and 0 (true and false)
# dp 长度是多少, 0 to target - 求组合（518）而不是求排列（322）
# dp[x] = dp[x - num] or dp[x] # 加入或不加入num去make up sum，加上dp[x]防止把true改成false(dp[x - num])
# dp[0] 是什么? 1

### 为什么0/1背包要倒序：
# 正序会发生什么
# 初始:dp = [True, False, False](dp[0]=True)
# 处理 num=1,内层 i 从小到大:
# i=1: dp[1] = dp[1] or dp[0]   # dp[0]=True → dp[1]=True
# i=2: dp[2] = dp[2] or dp[1]   # dp[1]=True → dp[2]=True ❌
# 问题出在 i=2 这步:它读的 dp[1] 是几秒钟前刚被同一枚 num=1 写过的值。翻译成人话,这个 True 的含义是:
# "dp[2] 可行,因为 dp[1] 可行(用了这枚 1),再加上这枚 1"
# ——同一枚 1 被数了两次。

# 倒序会发生什么
# 处理 num=1,内层 i 从大到小:
# i=2: dp[2] = dp[2] or dp[1]   # dp[1] 还是初始的 False → dp[2]=False ✅
# i=1: dp[1] = dp[1] or dp[0]   # dp[0]=True → dp[1]=True
# i=2 时读到的 dp[1] 是上一个物品处理完的状态(这里就是初始状态),num=1 还没机会污染它。等 dp[1] 变成 True 时,dp[2] 已经算完了,追不上了。



def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    # early return 
    if total % 2 == 1: # odd
        return False
    
    target = total // 2

    dp = [False] * (target + 1) # 组合数最小为0
    dp[0] = True # 空组合也是1个组合

    for num in nums:
        for i in range(target, num - 1, -1): #末尾不包含，所以只到num就停
            # if i >= num:
            dp[i] = dp[i - num] or dp[i] 

    return dp[target]
    


### ACM
# 输入格式(假设)
# 4
# 1 5 11 5
# 第一行 n,第二行 n 个整数。输出 true 或 false。

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = list(map(int, data[1:]))
    print(canPartition(nums))

main()



