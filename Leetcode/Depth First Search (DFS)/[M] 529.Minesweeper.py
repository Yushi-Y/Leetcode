
### ------------DFS (more natural for this Q)------------------
### Thoughts:
# The core question is: when do we recurse (expand), and when do we stop?

# Click on 'M' → mark 'X', return immediately
# Click on 'E' → count mines in all 8 neighbors

# If mines > 0 → write the digit, stop (don't recurse)
# If mines == 0 → mark 'B', recurse into all 8 'E' neighbors (neignbors must be empty for 'B')

# The "mark before recursing" step is your visited check — once a cell is 'B' or a digit, 
# it's no longer 'E', so you naturally won't revisit it.


### TC: O(m*n) - Worst case is an all-empty board where you touch every cell as 'B'.
### SC: O(m*n) - The recursion stack dfs(m, n). Worst case is again an all-empty board where the DFS chains through every cell
# dfs(0,0) → dfs(0,1) → dfs(0,2) → ... → dfs(m-1, n-1) — stack depth can reach m × n.

class Solution:
    def dfs(self, board, r, c):
        m, n = len(board), len(board[0])
        count = 0
        # edge cases
        if r >= m or c >= n or r < 0 or c < 0 or board[r][c] != 'E':
            return 

        # count mines in all 8 E neignbors
        for (nr, nc) in [(r, c+1), (r, c-1), (r+1, c), (r+1, c-1), (r+1, c+1), (r-1, c), (r-1, c+1), (r-1, c-1)]:
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                count += 1

        if count > 0:
            board[r][c] = str(count)
            return # do not recurse

        board[r][c] = 'B' # mark it to prevent revisiting
        # for each of 8 neignbors (nr, nc):
        for (nr, nc) in [(r, c+1), (r, c-1), (r+1, c), (r+1, c-1), (r+1, c+1), (r-1, c), (r-1, c+1), (r-1, c-1)]:
            self.dfs(board, nr, nc)

        

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # if board[r][c] == 'E':
        self.dfs(board, r, c)
        return board
        

        
# ### ------------BFS-----------------
### Thoughts: 
# Same logic as DFS, just iterative with a queue (adding to visited and queue) instead of recursive calls at 'B'. 
# Every 'E' → enqueued (add to queue) + added to visited → popped → marked 'B' or digit

### Use the classic pesudocode for BFS
# queue = [start]
# visited = {start}

# while queue:
#     node = queue.popleft()
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)


### Example
# initial click (0,0), all empty board

# queue   = [(0,0)]
# visited = {(0,0)}

# --- pop (0,0), count=0, mark 'B', enqueue neighbors ---

# queue   = [(0,1), (1,0), (1,1)]
# visited = {(0,0), (0,1), (1,0), (1,1)}

# --- pop (0,1), count=0, mark 'B', enqueue neighbors ---
# (0,0) already in visited → skip
# (1,1) already in visited → skip
# (1,2) new → add

# queue   = [(1,0), (1,1), (1,2)]
# visited = {(0,0), (0,1), (1,0), (1,1), (1,2)}

# ... and so on

# visited = every coordinate ever enqueued (grows monotonically, never shrinks)
# queue = coordinates waiting to be processed (shrinks as you popleft, grows as you enqueue)

# Visited keeps track of all 'E' cells that have been enqueued so far — so you never process the same cell twice. It stops spreading when: a cell has adjacent mines → mark digit, don't enqueue its neighbors; a cell is out of bounds; a cell is already in visited
# So BFS naturally forms the "revealed region" you see in real minesweeper — spreading until it hits numbered borders on all sides.


### TC: Same as DFS — each cell is visited at most once due to the visited set, so worst case you process every cell once.
# SC: O(m × n). Two things using space: visited set — at most m × n entries; queue — at most m × n entries at once

class Solution:
    def bfs(self, board, r, c):
        m, n = len(board), len(board[0])

        queue = deque([(r, c)])
        visited = {(r, c)} # a set, not a dict

        while queue:
            r, c = queue.popleft() # the visited 'E'

            # first reset count in while loop for each visited 'E'
            count = 0
            # count mines in all 8 E neignbors
            for (nr, nc) in [(r, c+1), (r, c-1), (r+1, c), (r+1, c-1), (r+1, c+1), (r-1, c), (r-1, c+1), (r-1, c-1)]:
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1

            if count > 0:
                board[r][c] = str(count) # do not add to queue

            else: 
                board[r][c] = 'B' # mark it to prevent revisiting
                # for each of 8 neignbors (nr, nc):
                for (nr, nc) in [(r, c+1), (r, c-1), (r+1, c), (r+1, c-1), (r+1, c+1), (r-1, c), (r-1, c+1), (r-1, c-1)]:
                    # IMPORTANT! Do bounding check before adding to queue - positive checks chained by AND not OR
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited: # not a visited 'E'
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                    


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # if board[r][c] == 'E':
        self.bfs(board, r, c)
        return board

        
### Difference between DFS and BFS (in minesweeper)
# The only difference is the order they visit cells:
# board:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# BFS order (level by level, outward):
# (0,0) → (0,1) (1,0) (1,1) → (0,2) (2,0) (2,1) (2,2)

# DFS order (go deep first, then backtrack):
# (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,1) → (2,0) → (1,0) → (1,1)

# But since every 'E' cell eventually gets marked 'B' or a digit in both cases, the final board looks the same.

# Think of it like exploring a maze:
# BFS — sends scouts in all directions simultaneously, expanding the frontier evenly
# DFS — picks one path and goes as deep as possible, then backtracks
# For this problem it doesn't matter which you use — same result, same TC/SC. The choice is just about style and recursion limit concerns of DFS.