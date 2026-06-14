# LeetCode 63 — Unique Paths II
# A robot is located at the top-left corner of an m x n grid. It can only move right or down at any step, and it's trying to reach the bottom-right corner.
# Now some cells contain obstacles. The grid is given as obstacleGrid, where obstacleGrid[i][j] == 1 means an obstacle and 0 means free space. The robot cannot move through obstacles.
# Return the number of unique paths from top-left to bottom-right.
# Example 1:
# Input: obstacleGrid = [[0,0,0],
#                        [0,1,0],
#                        [0,0,0]]
# Output: 2
# The obstacle in the middle blocks some routes — only Right→Right→Down→Down and Down→Down→Right→Right remain.
# Example 2:
# Input: obstacleGrid = [[0,1],
#                        [0,0]]
# Output: 1
# Constraints: 1 <= m, n <= 100, cell values are 0 or 1.

# df[i, j] = df[i-1, j] + df[i, j-1] 


## TC O(mn), SC O(mn)
class Solution:
    def uniquePaths(self, grid, m: int, n: int) -> int:
        df = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # if a cell is an obstacle, set its count to 0.
                if grid[i][j] == 1:
                    df[i][j] = 0 # path that passes through [i, j] will be zero
                # edge case
                elif i == 0 and j == 0:
                    df[i][j] = 1 # start point path = 1 if not an obstacle
                else:
                    from_top = df[i-1][j] if i > 1 else 0
                    from_left = df[i][j-1] if j > 1 else 0
                    df[i][j] = from_left + from_top

        return df[m-1][n-1]