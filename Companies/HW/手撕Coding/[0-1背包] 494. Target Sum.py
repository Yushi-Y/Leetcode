# 494. Target Sum
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

# Return the number of different expressions that you can build, which evaluates to target.
# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:
# Input: nums = [1], target = 1
# Output: 1

### Thoughts
# 设取正号的数之和为 P,取负号的数之和为 N。那么:

# P - N = target
# P + N = sum

# 两式联立,P 等于什么? P = (target + sum) // 2

# 于是问题变成:从 nums 中选一个子集,和恰好为 P,有几种选法——0/1 背包计数版（计combination）。

# dp[x] = num of combinations to make up x from nums
# dp[x] += dp[x - num] for num in nums
# dp length is P
# dp[0] = 1


###倒序： 494倒序是为了防止新更新的dp污染后面的dp，因为num只有一个，不是无限个(similar to 416)
# 倒序 = 保证算 dp[i] 时读到的 dp[i - num] 还是"没见过这枚 num 的旧世界",防止本轮的更新顺着数组往右传播——一旦传播,就等于同一个 num 被链式使用多次,而 494 里每个数只有一枚

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        two_P = sum(nums) + target

        # early return
        if two_P % 2 != 0 or two_P < 0:
            return 0
        
        P = two_P // 2
        
        dp = [0] * (P + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(P, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[P]




