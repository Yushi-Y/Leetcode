# Dynamic Programming (DP) is a method to solve problems by breaking them down into smaller overlapping subproblems, storing results, and reusing them instead of recalculating.
# dp[x]=minimum number of coins to make amount x
# Key formula: dp[x]=min​(dp[x−coin]+1)

# dp[1] = min(dp[0] + 1) = 1   → use coin 1
# dp[2] = min(dp[1] + 1, dp[0] + 1) = 1   → use coin 2
# dp[3] = min(dp[2] + 1, dp[1] + 1) = 2   → (2+1 or 1+1+1)
# dp[5] = 1 (use coin 5)
# ...
# dp[11] = min(dp[10] + 1, dp[9] + 1, dp[6] + 1) = 3

# Time complexity: O(n * m) - n is the amount, m is the number of coins
# Space complexity: O(n) - dp array

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x]=minimum number of coins to make amount x
        dp = [float('inf')] * (amount + 1) # dp array, start with 0
        dp[0] = 0

        # Create tables for DP
        for i in range(1, amount+1): # start from 1 as coin starts from one
            for coin in coins:
                if i - coin >= 0: # use >= not > as it includes dp[0] case when i = coin
                    dp[i] = min(dp[i], dp[i - coin] + 1) # min has to be between two values

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]