### Steps
# Since you need the shortest gap between two islands, think of it in two steps:
# Step 1: Find one island completely (using DFS)
# Step 2: Expand outward from it through water until you hit the other island (using BFS)

# Why DFS then BFS?
# DFS is good for "find everything connected to this cell" — perfect for mapping out one whole island.
# BFS is good for "shortest distance" — it expands one step at a time, so the first time it touches island 2, that's guaranteed to be the shortest path.


### Pseudocode
# Step 1: Find any cell belonging to island 1
# scan grid row by row
# when you find a 1, stop — this is your starting cell
# Step 2: DFS from that cell to mark all of island 1
# dfs(cell):
#     mark cell as 2
#     add cell to BFS queue
#     for each of 4 neighbours:
#         if neighbour is 1:
#             dfs(neighbour)
# Step 3: BFS outward from island 1
# steps = 0
# while queue not empty:
#     for each cell in current layer:
#         for each of 4 neighbours:
#             if neighbour == 1:        ← hit island 2!
#                 return steps
#             if neighbour == 0:        ← water, keep expanding
#                 mark as 2
#                 add to next layer
#     steps += 1

# The key ideas:

# Marking visited cells as 2 prevents revisiting
# BFS processes one full "ring" at a time before incrementing steps
# You *seed the queue* with all of island 1 so expansion starts from its entire border simultaneously


### TC: O(n*2)
# Every cell in the grid is visited at most once — once during DFS, once during BFS. Grid has n² cells total.

# SC: O(n²)
# Queue holds at most O(n²) cells
# DFS recursion stack can go O(n²) deep in the worst case (snake-shaped island) 
# recursion although not explicit data structure, still takes up memory:
# dfs(0,0)
#   → calls dfs(0,1)
#     → calls dfs(0,2)
#       → calls dfs(0,3)   ← stack is 4 frames deep here, this is recursion stack


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # step 1: Find any cell belonging to island 1
        start = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break  # breaks inner loop only
            if start: break # breaks outer loop

        # Step 2: DFS from that cell to mark all of island 1
        def dfs(i, j):
            grid[i][j] = 2 # mark as visited
            queue.append((i, j)) # seed the BFS queue with all of island 1 so expansion starts from its entire border simultaneously
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # bound check 
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj)

        dfs(*start) # * unpacks (i, j) into two args into DFS to be grammaly correct

        # Step 3: BFS outward from island 1
        steps = 0

        while queue: # not empty
            for _ in range(len(queue)): # want steps += 1 once per ring, not once per cell. this says "process exactly however many cells are in the queue RIGHT NOW" 
                i, j = queue.popleft() # so pop all cells in the queue right
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    # bound check
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:  # ← hit island 2!
                        return steps
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:  # ← water, keep expanding
                        grid[ni][nj] = 2 # mark visited
                        queue.append((ni, nj))
            steps += 1


        return steps

### why add 'for _ in range(len(queue)):'
# Without it:
# pop cell 1 → steps = 1
# pop cell 2 → steps = 2   ← WRONG, these are all ring 1
# pop cell 3 → steps = 3
# With it:
# pop cell 1, 2, 3, 4, 5 (whole ring 1) → steps = 1   ← correct
# pop cell 6, 7, 8 (whole ring 2) → steps = 2
                
