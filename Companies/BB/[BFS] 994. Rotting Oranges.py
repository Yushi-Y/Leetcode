# minimum number of minutes 
# shortest path to reach all oranges in the grid 
# unless an orange is unreachable
# move 4 directionally

### bfs
# queue = queue()
# visited = set()
# while queue: 
# node = queue.popleft() # the first element
# process(node)
# for neighbours of node:
#     if neighbour is not in visited():
#           queue.append(neighbour)

### pc
# check the grid - put all rotten oranges into the queue (store the coordinates)
# visited - all rotten oranges
# for every rotten orange in the queue: 
# process - move 4 directionally
# if orange is fresh - turn it rotten
# reduce frensh orange number by 1
# queue.append(rotten orange)

# keep count of fresh oranges
# if there are still fresh orange left - return -1
# else: return num of minutes

# TC: O(mn), SC: O(mn)

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0 # keep track of fresh oranges
        minutes = 0

        # put all rotten oranges into the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh_count += 1

        # edge case
        if fresh_count == 0:
            return 0

        # bfs
        while queue and fresh_count > 0: # one update
            minutes += 1

            # for every rotten orange in the queue (at this minute) 
            # queue - [i1, j1], [i2, j2]
            for _ in range(len(queue)):
                i, j = queue.popleft() # the first element
                # (-1, 0), (+1, 0), (0, -1), (0, +1)
                for di, dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                    i_new, j_new = i + di, j + dj

                    if 0 <= i_new < rows and 0 <= j_new < cols and grid[i_new][j_new] == 1:
                        grid[i_new][j_new] = 2
                        fresh_count -= 1
                        queue.append([i_new, j_new])

        return minutes if fresh_count == 0 else -1





