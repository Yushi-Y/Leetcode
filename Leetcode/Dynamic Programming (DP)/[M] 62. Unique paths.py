# There is a robot on an m x n grid. The robot starts at the top-left corner (grid[0][0]). The robot tries to reach the bottom-right corner (grid[m-1][n-1]).
# The robot can only move either one step down or one step right at any point in time.
# Given the two integers m and n, return the number of possible unique paths the robot can take to reach the bottom-right corner.
# Examples:
# Input:  m = 3, n = 7
# Output: 28

# Input:  m = 3, n = 2
# Output: 3
# Explanation: From the top-left, there are 3 ways to reach the bottom-right:
#              1. Right -> Down -> Down
#              2. Down -> Down -> Right
#              3. Down -> Right -> Down

# Quick intuition first: the robot only moves down or right, so any cell (i, j) can only be reached from the cell above it (i-1, j) or the cell to its left (i, j-1). That means:
# ways to reach (i, j) = ways to reach the cell above + ways to reach the cell on the left

# 2D DP
# dp[i][j] is the number of ways to reach (i, j)
# dp[i][j] = dp[i-1, j] + dp[i, j-1]


## TC O(mn), SC O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n grid, every cell starts at 1 (covers both base cases at once)
        dp = [[1]*n for _ in range(m)]

        # base cases
        # for i in range(m):
        #     dp[i, 0] = 1
        # for j in range(n):
        #     dp[0, i] = 1

        # fill from (1, 1) onward — row 0 and col 0 stay as the base case 1s
        for i in range(1, m):
            for j in range(1, n): 
                dp[i, j] = dp[i-1, j] + dp[i, j-1]

        return dp[m-1, n-1]
        