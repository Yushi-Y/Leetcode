# You are a robber planning to rob houses along a street. The houses are arranged in a straight line (not a circle this time). Each house has a stash of money, given in an array nums.
# The constraint: adjacent houses have connected security systems, so robbing two directly adjacent houses on the same night triggers the alarm.
# Given the integer array nums, return the maximum amount of money you can rob tonight without alerting the police.
# Examples:
# Input:  nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 0 (money=1) and house 2 (money=3) → total 4.

# Input:  nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Rob house 0 (1), house 2 (9), house 4 (1) → wait, that's 2+9+1=12.
#              Rob house 0 (money=2), house 2 (money=9), house 4 (money=1) → total 12.



# Dynamic Programming (DP) is a method to solve problems by breaking them down into smaller overlapping subproblems, storing results, and reusing them instead of recalculating.
# dp[i]=maximum cum. amount of money at the i-th house 
# Key formula: dp[i] = max(dp[i-2] + num[i], dp[i-1])
# dp[0]=nums[0]
# dp[1]=max(nums[1], dp[0])
# dp[2]=max(nums[2], dp[1])
# dp[3]=max(dp[1]+nums[3],dp[2])

# Time complexity: O(n) - n is the number of houses
# Space complexity: O(n) - dp array


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # if n >= 2:
        dp = [0] * n # Create the DP array
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


# Space-optimized solution 
# Only keep the previous two values prev2 and prev1
# Time complexity: O(n) - n is the number of houses
# Space complexity: O(1) - only keep the previous two values prev2 and prev1

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, n):
            current = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = current

        return prev1