# i = j + (i - j)
# no break, one break, further break
# dp[i] = max(dp[i], j * (i - j), dp[j] * (i - j))

# TC: O(n^2), SC: O(n)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), dp[j] * (i - j)) # need to keep previous best

        return dp[n]