# 给定不同面额的硬币数组 coins 和总金额 amount,返回凑成该金额所需的最少硬币个数。如果无法凑出,返回 -1。每种硬币数量无限。

# 示例:

# coins = [1,2,5], amount = 11  →  3   (5+5+1)
# coins = [2], amount = 3       →  -1
# coins = [1], amount = 0       →  0

# 约束:1 <= coins.length <= 12,1 <= coins[i] <= 2^31 - 1,0 <= amount <= 10^4


### Thoughts
# DP[i] = num of minimum coins sum to i
# for each coin, dp[i] = min(dp[i - coin] + 1, dp[i]) - whether to add this coin or not
# dp[0] = 0
# return dp[amount] or -1 if cannot make up - dp[amount] > amount


def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 2] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i > coin:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[amount] if dp[amount] != amount + 2 else -1




