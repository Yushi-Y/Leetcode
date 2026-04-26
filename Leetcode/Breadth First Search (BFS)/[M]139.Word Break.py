### BFS solution
# The key insight is: treat each INDEX in the string as a node. Index 0 is the start, index len(s) is the goal.
# Two nodes i and j are neighbors if s[i:j] is a word in the dictionary — meaning you can "jump" from position i to position j.
# So for s = "leetcode", wordDict = ["leet", "code"]:

# Node 0 has neighbor 4, because s[0:4] = "leet" is in the dictionary
# Node 4 has neighbor 8, because s[4:8] = "code" is in the dictionary
# If we reach node 8 (which equals len(s)), the string can be broken into words


### BFS pesudo code
# queue = [start]
# visited = {start}

# while queue:
#     node = queue.popleft()
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)

# Option 1: use pop(0) — works but slow, O(n)
# queue = [0]
# node = queue.pop(0)

# # Option 2: use deque — has popleft(), O(1)
# queue = deque([0])
# node = queue.popleft()
# pop(0) does the same thing — removes from the front — but it's O(n) because Python has to shift every remaining element one spot to the left. With a deque, popleft() is O(1), no shifting needed.
# For interview purposes, always use deque. It shows you understand the efficiency difference.
# deque stands for "double-ended queue." It's just a list that's optimized for adding/removing from both ends.
# Why not use a regular list? Because with a normal list, list.pop(0) is O(n) — Python has to shift every element over. With a deque, deque.popleft() is O(1).

# Time: O(n² · m)
# We visit at most n nodes (indices 0 to n-1)
# At each node, we try up to n substrings
# Each substring hash/comparison takes up to m (average word length)

# Space: O(n)
# Queue holds at most n indices
# Visited set holds at most n indices
# Where n = len(s) and `m = average word length in the dictionary.

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        queue = deque([0])
        visited = {0} # a set

        while queue:
            node = queue.popleft()
            # for neighbor in node.neighbors:
            for j in range(node + 1, len(s)+1):
                if s[node:j] in wordSet: # it is a neignbor, set is O(1) look up, list is O(n)
                    if j == len(s): # reach the end
                        return True
                    if j not in visited:
                        visited.add(j) # set use .add not .append
                        queue.append(j)

        return False

                