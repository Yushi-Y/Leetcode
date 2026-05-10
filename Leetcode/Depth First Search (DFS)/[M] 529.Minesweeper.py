
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
### Thoughts: use the classic pesudocode for BFS
# Same logic as DFS, just iterative with a queue instead of recursive calls at 'B'. 
# queue = [start]
# visited = {start}

# while queue:
#     node = queue.popleft()
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)


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
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited: # and board[nr][nc] == 'E'
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

        

