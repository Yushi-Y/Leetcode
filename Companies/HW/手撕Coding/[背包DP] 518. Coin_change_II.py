# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return ''the number of combinations'' that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.
# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1

### Thoughts
# dp[x] = num of combinations that make up x
# dp[x] = sum(dp[x - coin]) for each coin value

# 322外层是 amount、内层是 coins。用 coins=[1,2], amount=3 想:算 dp[3] 时,coin=1 的路径(...+1)和 coin=2 的路径(...+2)都会被加进来,意味着 1+2 和 2+1 被分别计数——你数出来的是排列(这其实是 377 的答案)。
# 要数组合,需要外层遍历 coins、内层遍历 amount
# 先只用 coin=1 把整个表填一遍,再引入 coin=2 更新一遍……这样任何一种方案里,硬币被"引入"的顺序是固定的(按 coins 数组顺序)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x]=num of combinations of coins to make amount x
        dp = [0] * (amount + 1) # dp array, start with 0
        dp[0] = 1 # 空组合（0硬币）也是一种组合

        # Create tables for DP
        for coin in coins:
             for i in range(coin, amount+1): # start from 1 as coin starts from one
                # if i - coin >= 0: 
                    dp[i] += dp[i - coin] # add the comination number with that coin

        return dp[amount] 
    