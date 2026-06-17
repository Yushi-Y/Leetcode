# LeetCode 1230 — Toss Strange Coins
# You have some coins. The i-th coin has a probability prob[i] of facing heads when tossed. Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.
# Example 1
# Input:  prob = [0.4], target = 1
# Output: 0.40000
# Example 2
# Input:  prob = [0.5, 0.5, 0.5, 0.5, 0.5], target = 0
# Output: 0.03125
# Constraints

# 1 <= prob.length <= 1000
# 0 <= prob[i] <= 1
# 0 <= target <= prob.length
# Answers within 1e-5 of the correct answer are accepted.


### Thoughts
# i means the i-th coin; j is the target of heads
# dp[i][j]: prob of j heads after tossing i coins

# dp[0][0] = 1 (0 coin, 0 head)

# if toss coin i, get head: 
# dp[i][j] += dp[i-1][j-1] * prob(i-1)
# elif toss coin i, get tail: 
# dp[i][j] += dp[i-1][j] * (1 - prob(i-1))

# return dp[n][target], n = number of coins

### TC O(n*target) - for loop, SC O(n*target) - DP table

def probabilityOfHeads(self, prob: List[float], target: int) -> float:
    n = len(prob)

    dp = [[0] * (target + 1) for _ in range(n)]
    # starting case
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # if toss coin i, get head
            dp[i][j] += dp[i-1][j-1] * prob(i-1) if j > 0 else 0 
            # if toss coin i, get tail
            dp[i][j] += dp[i-1][j] * (1 - prob(i-1))

    return dp[n][target]


# Worth knowing for interviews — since each row only reads from the row above, you can collapse to 1D. Iterate j downward so you don't overwrite values you still need:
### TC O(n*target) - for loop, SC O(target) only - DP array

# def probabilityOfHeads(self, prob: List[float], target: int) -> float:
#     dp = [1.0] + [0.0] * target
#     for p in prob:
#         for j in range(target, -1, -1):
#             dp[j] = dp[j] * (1 - p) + (dp[j - 1] * p if j > 0 else 0)
#     return dp[target]
