class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        column = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= column or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            area += dfs(r - 1, c)
            area += dfs(r, c - 1)
            area += dfs(r + 1, c)
            area += dfs(r, c + 1)

            return area

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
