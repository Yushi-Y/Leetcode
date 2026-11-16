# Connected components problem using DFS on a 2D grid.
# recursive DFS
# dfs(node, visited):
# if node is not in visited:
# process(node)
# for neighbour of node:
# if neighour not in visted:
# dfs(neighbour, visted)

### pseudocode
# for every i, j in grid: 
# check grid[i][j] == '1': # land
# dfs[i, j] - sink this island - should turn every 2d point into 0 - so mark it as visited
# process(grid[i][j]) - move 4 directionally with dfs(i, j)
# continue until the whole grid is processed


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_of_islands = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
                return 

            grid[i][j] = '0' # sink the island

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_of_islands += 1
                    dfs(i, j)

        return num_of_islands


        



# # dfs(r, c) defines the depth first search action
# # TC: O(M × N) — every cell visited at most once
# # SC: O(M × N) — worst case recursion depth if the entire grid is land (one giant island, stack goes M×N deep)


