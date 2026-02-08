# connected components problem using DFS on a 2D grid.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # empty grid
            return 0

        row = len(grid)
        column = len(grid[0])
        islands = 0

        def dfs(r, c):
            # out of bounds or no islands
            if r < 0 or r >= row or c < 0 or c >= column or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands


