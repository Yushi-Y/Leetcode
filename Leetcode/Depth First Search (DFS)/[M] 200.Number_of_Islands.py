# Connected components problem using DFS on a 2D grid.
# dfs(r, c) defines the depth first search action
# TC: O(M × N) — every cell visited at most once
# SC: O(M × N) — worst case recursion depth if the entire grid is land (one giant island, stack goes M×N deep)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None

        row = len(grid)
        col = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r > row or c < 0 or c > col:
                return 

            if grid[r][c] == 0:
                return # stopping condition

            grid[r][c] = 0 # mark as visited

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands 

