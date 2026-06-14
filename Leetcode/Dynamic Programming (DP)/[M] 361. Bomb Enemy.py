# Given an m x n matrix grid where each cell is one of:

# 'W' — a wall
# 'E' — an enemy
# '0' — an empty cell

# Return the maximum number of enemies you can kill using one bomb. You can only place the bomb in an empty cell ('0').
# When detonated, the bomb kills all enemies in the same row and same column as the planted cell, traveling outward in all four directions until it hits a wall (walls block the blast and cannot be destroyed).
# Example:
# grid = [["0","E","0","0"],
#         ["E","0","W","E"],
#         ["0","E","0","0"]]
# → 3   (place at row 1, col 1: kills E above, E left, E below = 3)


## greedy approach - ineffcient TC O(m*n*(m+n)), SC O(1) though - only count, k, j etc, no m*n DP table/array storage
def maxKilledEnemies(grid: list[list[str]]) -> int:
    maxkill = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0': # empty
                count = 0 
                # count enemies up
                k = i - 1
                while k >= 0 and grid[k][j] != 'W':
                    if grid[k][j] == 'E':
                        count += 1
                    k -= 1
                # count enemies down
                k = i + 1
                while k < rows and grid[k][j] != 'W':
                    if grid[k][j] == 'E':
                        count += 1 
                    k += 1
                # count enemies left
                k = j - 1
                while k >= 0 and grid[i][k] != 'W':
                    if grid[i][k] == 'E':
                        count += 1 
                    k -= 1
                # count enemies right
                k = j + 1
                while k < cols and grid[i][k] != 'W':
                    if grid[i][k] == 'E':
                        count += 1 
                    k += 1

                maxkill = max(maxkill, count)

    return maxkill



### DP approach

# What the brute force does. For each empty cell it launches four fresh walks outward to the walls. The fatal redundancy: cells in the same wall-bounded zone re-walk the same enemies. 

### DP thoughts
# Why the second is DP. **The defining feature of DP is a recurrence: each subproblem's answer is built from a smaller already-solved one, computed once and stored. ** Look at the left table:
# left[i][j] = left[i][j-1] + 1   if grid[i][j] == 'E'
#            = 0                  if grid[i][j] == 'W'
#            = left[i][j-1]       otherwise
# That's a textbook recurrence. It's genuinely DP: overlapping subproblems (every empty cell in a zone needs the same partial sums) solved once and reused, 
# which is exactly what the brute force failed to do.

# Why it's more efficient. The brute force recomputes a zone's enemy count from scratch at every empty cell. 
# **The DP computes each cell's directional count in O(1) by reading the adjacent cell's already-stored result — the recurrence above does one comparison and one add. **
# Building each table touches every cell once (O(mn)), four tables is still O(mn), and the final aggregation scan is another O(mn). Total O(mn) time.
# The trade-off is space: you store four full grids, so O(mn) extra space, versus the brute force's O(1). 
# That's the classic DP bargain — spend memory to store subproblem answers so you never recompute them.


## pseucodecode for DP
# create 4 DP tables
# for each row:
      # for each col (left - right): count E until W, store in left[i][j]
      # for each col (right - left): count E until W, store in right[i][j]
# for each col:
      # for each row (up - down): count E until W, store in up[i][j]
      # for each row (down - up): count E until W, store in down[i][j]

# for each E:
      # maxkill = max(maxkill, left + right + up + down)

    
## TC O(mn) for two for loops, SC O(mn) for DP arrays
def maxKilledEnemies(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    maxkill = 0

    rows = len(grid)
    cols = len(grid[0])

    # create four-directional DP table
    left = [[0] * cols for _ in range(rows)]
    right = [[0] * cols for _ in range(rows)]
    up = [[0] * cols for _ in range(rows)]
    down = [[0] * cols for _ in range(rows)]

    # left: accumulate across each row, left -> right
    for i in range(rows):
        count = 0 # recount for each row
        for j in range(cols):
            if grid[i][j] == 'W':
                count = 0
            elif grid[i][j] == 'E':
                count += 1
            left[i][j] = count 

    # right: accumulate across each row, right -> left
    for i in range(rows):
        count = 0
        for j in reversed(range(cols)):
            if grid[i][j] == 'W':
                count = 0
            elif grid[i][j] == 'E':
                count += 1
            right[i][j] = count 


    # up: accumulate across each col, up -> down
    for j in range(cols):
        count = 0
        for i in range(rows):
            if grid[i][j] == 'W':
                count = 0
            elif grid[i][j] == 'E':
                count += 1
            up[i][j] = count 

    
    # down: accumulate across each col, down -> up
    for j in range(cols):
        count = 0
        for i in reversed(range(rows)):
            if grid[i][j] == 'W':
                count = 0
            elif grid[i][j] == 'E':
                count += 1
            down[i][j] = count 

    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                total = 0
                # add edge cases
                # recurrance from 1-step sub-problems already solved
                if j >= 1: total += left[i][j-1] 
                if j < cols-1: total += right[i][j+1]
                if i >= 1: total += up[i-1][j]
                if i < rows-1: total += down[i+1][j]
                maxkill = max(maxkill, total)

    return maxkill



