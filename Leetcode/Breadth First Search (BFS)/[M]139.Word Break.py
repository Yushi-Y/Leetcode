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

### Time: O(n² · m)
# We visit at most n nodes (indices 0 to n-1)
# At each node, we try up to n substrings (whether in dict)
# Each substring hash/comparison takes up to m (average word length)

# Space: O(n)
# Queue holds at most n indices
# Visited set holds at most n indices
# Where n = len(s) and `m = average word length in the dictionary.

### Code
# from collections import deque

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         wordSet = set(wordDict)
#         queue = deque([0])
#         visited = {0} # a set, so no duplicates - what has been visited

#         while queue:
#             node = queue.popleft()
#             # for neighbor in node.neighbors:
#             for j in range(node + 1, len(s)+1):
#                 if s[node:j] in wordSet: # it is a neignbor, set is O(1) look up, list is O(n)
#                     if j == len(s): # reach the end
#                         return True
#                     if j not in visited: # only if not visited before, add to queue
#                         visited.add(j) # set use .add not .append
#                         queue.append(j)

#         return False

                
#--------------------- DP solution ----------------------
# dp[i] answers: "can s[0:i] be broken into dictionary words?"
# We want dp[len(s)] to be True.
# dp[0] = True   # empty string is always valid (base case)
# For each position i, we look back at every earlier position j. If dp[j] is True AND s[j:i] is a word in the dictionary, then dp[i] = True.

### Mapping to the template:
# dp = array of size (n+1), initialized to False
# dp[0] = True  # base case

# for i in range(1, n+1):
#     for each subproblem that builds into i:
#         if dp[subproblem] and transition is valid:
#             dp[i] = True

# return dp[n]

# dp = array of size (n+1), initialized to False
# dp[0] = True                          # base case: empty string

# for i in range(1, n+1):               # for each position
#     for j in range(0, i):             # look back at every earlier position
#         if dp[j] and s[j:i] in wordSet:   # subproblem solved AND valid transition?
#             dp[i] = True
#             break                     # no need to check further

# return dp[n]

### Walkthrough with s = "leetcode", wordDict = ["leet", "code"]:
# dp[0] = True

# i=1: "l"         → no match → dp[1] = False
# i=2: "le"        → no match → dp[2] = False
# i=3: "lee"       → no match → dp[3] = False
# i=4: dp[0]=True, s[0:4]="leet" ✅  → dp[4] = True
# i=5: no combo works                → dp[5] = False
# i=6: no combo works                → dp[6] = False
# i=7: no combo works                → dp[7] = False
# i=8: dp[4]=True, s[4:8]="code" ✅  → dp[8] = True

# return dp[8] = True ✅


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True  # base case

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in wordSet: # look up in set is O(1) vs O(n) in list
                    dp[i] = True
                    break # The break is optional but saves time — once you know dp[i] is True, no point checking more j values.

        return dp[len(s)]


### Time: O(n² · m)
# Outer loop: n iterations
# Inner loop: up to n iterations
# Each s[j:i] substring creation + set lookup: O(m)

# Space: O(n + k)
# dp array: O(n)
# wordSet: O(k) where k = total characters stored in wordDict/O(W · m) where W = number of words, m = average word length

# Same time complexity as BFS, just a different way of thinking about it.
            