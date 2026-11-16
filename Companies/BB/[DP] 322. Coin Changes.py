# Dynamic Programming (DP) is a method to solve problems by breaking them down into smaller overlapping subproblems, storing results, and reusing them.
# bottom up DP
# dp[x]=minimum number of coins to make amount x
# Key formula: dp[x] = min(dp[x], dp[x - coin] + 1)

# dp[0] = 0
# dp[1] = dp[0] + 1 = 1 - use coin 1
# dp[2] = min(dp[1] + 1, dp[0] + 1) = 1 - use coin 2
# dp[3] = min(dp[1] + 1, dp[2] + 1) = 2 - (1, 2) or (2, 1)
# dp[4] = -1
# dp[5] = min(dp[3] + 1, dp[4] + 1, dp[0] + 1) = 1 - use coin 5
# ...
# dp[11] = min(dp[10] + 1, dp[9] + 1, dp[6] + 1) = 3

# m is amount, n is len(coins)
# TC: O(m*n)
# SC: O(m)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]=minimum number of coins to make amount i

        # define the DP array
        dp = (amount + 1) * [float('inf')]

        # define dp[0]
        dp[0] = 0

        # fill in the DP table
        for i in range(0, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
