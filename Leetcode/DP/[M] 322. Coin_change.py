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

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # dp[x]=minimum number of coins to make amount x
#         dp = [float('inf')] * (amount + 1) # dp array, start with 0
#         dp[0] = 0

#         # Create tables for DP
#         for i in range(1, amount+1): # start from 1 as coin starts from one
#             for coin in coins:
#                 if i - coin >= 0: # use >= not > as it includes dp[0] case when i = coin
#                     dp[i] = min(dp[i], dp[i - coin] + 1) # min has to be between two values

#         return dp[amount] if dp[amount] != float('inf') else -1
    



### Lingshen solution 2
# def unbounded_packback(capability: int, w: List[int], v: List[int]) -> int:
#     n = len(w)

#     @cache
#     def dfs(i, c):
#         if i < 0:
#             return 0
#         if c < w[i]:
#             return dfs(i - 1, c)
#         return max(dfs(i - 1, c), dfs(i, c - w[i]) + v[i])
    
#     return dfs(n - 1, capability)



#  f[i][c] = minimum number of coins to make amount c using first i coins
#  f[i + 1][c] = min(f[i][c], f[i + 1][c - coin] + 1)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            n = len(coins)

            f = [float('inf') * (amount + 1) for _ in range(n + 1)]
            f[0][0] = 0
            for i, x in enumerate(coins):
                  for c in range(amount + 1):
                        if c < x: 
                              f[i + 1][c] = f[i][c]
                        else:
                            f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)

            return f[n][amount] if f[n][amount] != float('inf') else -1

            # @cache
            # def dfs(i, c):
            #     if i < 0:
            #         return 0
            #     if c < w[i]:
            #         return dfs(i - 1, c)
            #     return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
            
            # return dfs(n - 1, amount)




### Lingshen solution 3
#  f[c] = minimum number of coins to make amount c 
#  f[c] = min(f[c], f[c - coin] + 1)

#  unbounded knapsack (each coin used infinite times)
#  so c is traversed from small to large
# When we update `f[c]`, we read from `f[c - x]` which **may have been updated** in this iteration
# This allows us to use the same coin multiple times

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            n = len(coins)

            f = [float('inf')] * (amount + 1) 
            f[0] = 0

            for x in coins:
                  for c in range(amount, x - 1, -1):
                        f[c] = min(f[c], f[c - x] + 1)

            return f[amount] if f[amount] != float('inf') else -1

            # @cache
            # def dfs(i, c):
            #     if i < 0:
            #         return 0
            #     if c < w[i]:
            #         return dfs(i - 1, c)
            #     return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
            
            # return dfs(n - 1, amount)