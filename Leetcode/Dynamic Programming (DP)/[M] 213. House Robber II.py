# House Robber II (LeetCode 213)
# You are a robber planning to rob houses along a street. The houses are arranged in a circle — meaning the first house is the neighbor of the last one. Each house has a stash of money, given in an array nums.
# The constraint: adjacent houses have connected security systems, so robbing two adjacent houses on the same night triggers the alarm.
# Given the integer array nums, return the maximum amount of money you can rob tonight without alerting the police.
# Examples:
# Input:  nums = [2, 3, 2]
# Output: 3
# Explanation: You cannot rob house 0 (money=2) and house 2 (money=2),
#              because they are adjacent (circular).

# Input:  nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 0 (money=1) and house 2 (money=3) → total 4.

# Input:  nums = [1, 2, 3]
# Output: 3
# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
            return 0
    if n == 1: 
        return nums[0]      # circle of one
    return max(rob_linear(nums[0 : n-1]),rob_linear(nums[1 : n])) # in a circle, house 0 and house n-1 are neighbors, so you can never rob both

def rob_linear(houses):
    # standard House Robber I
    prev2, prev1 = 0, 0
    for x in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + x)

    return prev1