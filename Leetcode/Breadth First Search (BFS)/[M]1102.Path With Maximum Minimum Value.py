### Thinking
# 1. 理解目标

# 我要从 A 到 B，最小值要尽量大

# → 这是一个 "最大化瓶颈" 问题

# 2. 想暴力解

# 遍历所有路径，记录每条路径的最小值，取最大

# → 可行但太慢，指数级

# 3. 想优化

# 有没有办法不走冤枉路？

# → 每次都走当前最大的格子 → 贪心 → 需要快速找最大 → heap

# 4. 确认贪心正确

# 如果我总是走最大的格子，会不会错过更好的路径？

# → 不会，因为走小的格子只会让最小值更小


### Question Type
# BFS 用队列决定遍历顺序：
# 普通 BFS:   queue → 先进先出，找最短路径
# 这道题:     heap  → 每次取最大值，找最优路径
# 本质还是在遍历图，只是把 queue 换成了 heap，所以也叫：
# Dijkstra 变体 或 优先队列 BFS (Priority Queue BFS)


### Heap
# 23:27Claude responded: A heap is a binary tree with one rule:A heap is a binary tree with one rule:

# Every parent is always larger (or smaller) than its children

# That's it — only the top is guaranteed
# Min-Heap:        Max-Heap:
#      1                9
#     / \              / \
#    3   2            7   8
#   / \              / \
#  7   4            3   4

# top = always min  top = always max

# NOT a sorted list
# Sorted: [1, 2, 3, 4, 5, 6, 7]   ← every element in order
# Heap:   [1, 3, 2, 7, 4, 5, 6]   ← only top is guaranteed

# Why use it
# You only care about "what's the best element right now" — not the full order. Heap does less work than sorting, so it's faster for inserts.
# OperationSorted ListHeapInsertO(n)O(log n)Get min/maxO(1)O(1)Remove min/maxO(n)O(log n)

# One liner: A heap is a lazy sorted list — it only guarantees the next best element, nothing else.


### BFS template
# queue = [start]
# visited = {start}

# while queue:
#     node = queue.popleft()
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)


### Pseudocode
# initialize:
#     heap = [(grid[0][0], 0, 0)]    # max-heap
#     visited[0][0] = True
#     min_val = grid[0][0]

# loop:
#     pop the largest value cell (val, r, c) from heap
#     min_val = min(min_val, val)
    
#     if reached bottom-right:
#         return min_val
    
#     for each of 4 neighbors:
#         if not visited:
#             push into heap


### What does heap and visited do
# Heap

# "What cells should I visit next, in what order?"
# Stores cells that are discovered but not yet processed
# Ordered by value — largest always at top
# Can have multiple cells waiting at the same time


# Visited
# "Have I already processed this cell?"
# Prevents visiting the same cell twice
# Just a True/False grid

# Timeline of a cell
# undiscovered → in heap → visited
#                (waiting)  (done)



### how does bfs and dfs differ in grid traversal logic
# BFS                           # DFS
# from collections import deque

# queue = deque([(0,0)])        stack = [(0,0)]
# visited[0][0] = True          visited[0][0] = True

# while queue:                  while stack:
#     r, c = queue.popleft()        r, c = stack.pop()
    
#     for dr, dc in dirs:           for dr, dc in dirs:
#         nr, nc = r+dr, c+dc           nr, nc = r+dr, c+dc
#         if valid and               if valid and
#         not visited[nr][nc]:       not visited[nr][nc]:
#             visited[nr][nc] = True     visited[nr][nc] = True
#             queue.append((nr,nc))      stack.append((nr,nc))
# Only difference: popleft() vs pop()

# How they explore differently
# Grid:
# 1 2 3
# 4 5 6
# 7 8 9

# BFS order:        DFS order:
# 1 2 4 3 5 7 ...   1 2 3 6 5 4 7 8 9
# ↑ spreads out     ↑ goes deep first
#   level by level    one direction first

# Start at 1, neighbors are 2 and 4

# BFS:                      DFS:
# push 2, 4                 push 2, 4
# [2, 4]                    [2, 4]

# popleft → 2  (oldest)     pop → 4  (newest)
# explore 2's neighbors     explore 4's neighbors first
# → spreads wide            → goes deep

# BFS = queue = first in first out = explores level by level
# DFS = stack = last in first out = explores depth first


### TC and SC
# TC (heap): O(mn log mn)
# mn cells total
# each cell → one push + one pop
# each push/pop on heap → O(log(heap size))
# heap size at most mn
# → O(mn log mn)

# SC
# O(mn) — comes from 3 things:
# visited array  →  O(mn)
# heap           →  O(mn)   ← at most all cells inside
                 

import heapq

class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        # [grid value, row, col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)] # default to not visited
        heap = [-grid[0][0], 0, 0] # max-heap
        visited[0][0] = True
        min_value = grid[0][0]

        while heap:
            val, r, c = heapq.heappop(heap) # similar to queue in BFS, but always pop the largest element
            min_value = min(min_value, -val)

            # boundary check first
            if r == m - 1 and c == n - 1:
                return min_value # the only return happens here
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # bound checks
                if 0 < nr <= m and 0 < nc <= n and visited[nr][nc] == False:
                    visited[nr][nc] = True # mark visited
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))# add neignbor to be processed


