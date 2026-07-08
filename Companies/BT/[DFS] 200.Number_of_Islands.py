# LeetCode 200 — Number of Islands
# Given an m x n 2D binary grid grid of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
# Example 1:
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# Constraints:

# m == grid.length, n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'


### Thoughts
# 初始岛屿熟练 = 0
# 遍历整个网络，遇到1，岛屿数量 + 1， 用dfs去淹没所有相邻的1 - mark it as '0'
# DFS recursively move in four directions（上下左右）
# return 岛屿数量

def numIslands(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    num_island = 0

    def dfs(r, c):
        if r < 0 or r > m or c < 0 or c > n or grid[r][c] == '0': # last is stopping condition of dfs
            return 
        
        grid[r][c] = '0' # sink this node

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                num_island += 1
                dfs(r,c)

    return num_island


### BFS
import deque

# queue = [start]
# visited = {start}

# while queue:
#     node = queue.popleft()
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)

def bfs(r, c):
        q = deque([(r, c)])
        grid[r][c] = '0'          # mark on enqueue
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'   # mark before pushing
                    q.append((nr, nc))


### ACM
# 输入格式

# 第 1 行：两个整数 m n（行数、列数），空格分隔
# 接下来 m 行：每行一个长度为 n 的字符串，只含 0/1，无空格

# 输出：一个整数（岛屿数量）
# 样例输入：
# 4 5
# 11110
# 11010
# 11000
# 00000


import sys


def main():
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    grid = [list(data[2 + i]) for i in range(m)]
    num_island = numIslands(grid)
    print(num_island)


main()


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         row, col = len(grid), len(grid[0])
#         num_of_island = 0

#         def dfs(r, c):
#             # edge case - out of bounds or no longer an island
#             if r < 0 or r > row or c < 0 or c > col or grid[r][c] == '0':
#                 return
#             grid[r][c] = '0'# mark this island as visited
#             # recursive dfs in four directions
#             dfs(r-1, c)
#             dfs(r+1, c)
#             dfs(r, c-1)
#             dfs(r, c+1)

            

#         for r in range(row):
#             for c in range(col):
#                 if grid[r][c] == '1':
#                     num_of_island += 1
#                     dfs(r,c)
        
#         return num_of_island



# Connected components problem using DFS on a 2D grid.
# dfs(r, c) defines the depth first search action
### TC: O(M × N) — every cell visited at most once
### SC: O(M × N) — worst case recursion depth if the entire grid is land (one giant island, recursive stack goes M×N deep)