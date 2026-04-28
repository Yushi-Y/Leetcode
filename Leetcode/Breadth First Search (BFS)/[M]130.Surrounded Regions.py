#---------------- DFS --------------------
### The key insight: instead of finding surrounded regions, find the unsurrounded ones (connected to a border 'O') and mark them safe ('T'). Everything else gets captured.

# DFS/BFS from every 'O' on the border — mark those cells as safe ('T')

# Sweep the entire board:
# 'O' → 'X' (surrounded, captured)
# 'T' → 'O' (restore border-connected cells)

# So dfs(r, c) means "visit the cell at row r, column c." Instead of a single node like in the generic pseudocode, here each node is a grid cell identified by two coordinates.
# The mapping to the general pseudocode is:
# Generic DFS:                    Grid DFS:

# node              →             (r, c)
# neighbors of node →             (r+1,c), (r-1,c), (r,c+1), (r,c-1)
# visited check     →             board[r][c] != 'O'
# mark visited      →             board[r][c] = 'T'

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m, n = len(board), len(board[0])

#         # dfs to mark 'O' to 'T'
#         def dfs(r, c):
#             if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O': # Rows go 0 to m-1, so r == m is already out of bounds.
#                 return 

#             board[r][c] = 'T' # mark every 'O' as 'T'

#             # recursion! Go depth first
#             dfs(r + 1, c) # turning every O connected to it into T
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)
            

#         # sweep the board - start dfs at border 'O's
#         for r in range(m):
#             for c in range(n):
#                 if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == 'O': 
#                     dfs(r, c) # only dfs on border O

# # After DFS runs, every cell on the board is one of three things:

# # 'X' — was always X, leave it alone
# # 'T' — an O connected to the border, needs to be restored
# # 'O' — an O not connected to the border, meaning it's surrounded

#         for r in range(m):
#             for c in range(n):
#                 if board[r][c] == 'O':
#                     board[r][c] = 'X' # captured
#                 if board[r][c] == 'T':
#                     board[r][c] = 'O' # border restored


### Time Complexity: O(m × n)
# The border loop visits at most 2m + 2n cells
# DFS visits each cell at most once (once marked 'T', it's skipped)
# The final sweep visits every cell once
# Total: O(m × n)

# Space Complexity: O(m × n)
# The only extra space is the recursion stack from DFS
# Worst case: every cell is 'O', DFS chains through all of them
# Stack depth = m × n


### why DFS?

# The core task is: find all 'O' cells connected to the border. That's fundamentally a "find connected components" problem, which is exactly what DFS (or BFS) is built for.
# Why it fits:
# Connectivity is the question. A border 'O' might connect to dozens of interior 'O's through a chain. You need to follow that entire chain. DFS naturally follows a path as far as it goes, marking every connected cell along the way.


#---------------- BFS --------------------

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
            
        # step 1 - collect all border O's
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == 'O': 
                    q.append((r,c)) 
                    board[r][c] = 'T'

        # step 2 - bfs inbound to find O's that connect to border O, mark as T
        while q: # q is not empty - keep processing until the queue is empty
            r, c = q.popleft()
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    q.append((nr, nc))


        # step 3 - update 
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X' # captured
                elif board[r][c] == 'T':
                    board[r][c] = 'O' # border restored



# Why BFS over DFS?
# The logic and time complexity are identical. The difference is practical:
# DFS risk — stack overflow:
# O O O O O O O O O O
# O O O O O O O O O O
# O O O O O O O O O O    ← 1000 x 1000 board of all O's
# ...
# Recursive DFS goes 1,000,000 calls deep. Python's default recursion limit is ~1000. This crashes.
# BFS avoids this. The queue grows wide, not deep. It uses heap memory (which is much larger) instead of the call stack (which is limited).
# DFS:  call → call → call → call → ... → 1M deep stack → crash
# BFS:  queue stores neighbors level by level → no stack issue
# Summary:
# DFSBFSTimeO(m×n)O(m×n)SpaceO(m×n) stackO(m×n) queueStack overflow riskYesNoCode simplicitySlightly simplerSlightly more code
# For interviews, mention both and say you'd prefer BFS for large grids to avoid stack overflow. That shows awareness of practical tradeoffs.