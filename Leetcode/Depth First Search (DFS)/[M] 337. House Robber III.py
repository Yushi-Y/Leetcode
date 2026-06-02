# Binary tree: it's a collection of nodes, where each node holds a value and points down to at most two other nodes — a left child and a right child. That's all "binary" means: at most two children per node. It branches downward and never loops back.


### Thoughts
# The core choice. Stand at any single node and ask: do I rob this node, or skip it? Just two options.

# If I rob it: I pocket its money, but now both of its children are off-limits (they're directly linked to me).
# If I skip it: my children are unconstrained — each is free to be robbed or not, whichever is better for it.

# That's the entire decision, *repeated at every node*.
# To make the choice at a node, what do I need to know from each child? Notice it's not just "what's the best my child's subtree can do." It's two different numbers:

# the best that child's subtree can do if the child itself gets robbed, and the best if the child itself is skipped.

# So every node reports a pair upward: (rob_me, skip_me).
# Given a node whose left child reported (L_rob, L_skip) and right child reported (R_rob, R_skip):

# rob_me = node.val + L_skip + R_skip
# (I take my money; my kids must stand down)
# skip_me = max(L_rob, L_skip) + max(R_rob, R_skip)
# (I take nothing; each kid does its own best)
# The final answer at the root is max(rob_root, skip_root).

# Why this is fast. Each node is visited once and produces its pair from its children's pairs — no recomputation. That's O(N). 
# The shape of the traversal matters: you compute children before the parent — you can't fill in a node's report card until both kids have handed theirs up. That's a post-order DFS (left, right, then me).

# Post-order DFS: When you DFS a tree, at every node you do three things: process this node, recurse left, recurse right. The only question is the order — specifically, when do you process the current node relative to its two children? That's what pre/in/post refer to:

# Pre-order — node first, then left, then right. ("Handle me, then go down.")
# In-order — left, then node, then right. (Node sits between the children; mainly used on BSTs to get sorted order.)
# Post-order — left, then right, then node last. ("Go all the way down first; handle me only after both children are done.")


### TC: n is number of nodes
# TC O(n) - Each node is visited exactly once, and at each node you do constant work: two adds, two maxes, build a 2-tuple. No copying, no recomputation. N nodes × O(1) each = O(N).
# SC O(h) - recursion, h is height of tree, which is ~ O(n) is the tree is skewed
# Why recursion costs space? Because every paused function call has to be remembered, and the rememberings pile up.
# The mechanism. When dfs(root) calls dfs(root.left), the outer call doesn't finish and vanish — it's stuck waiting for the inner call to hand back a result (it literally can't compute rob_me until L_rob, L_skip come back). So the computer has to save the outer call's state — its node, its local variables, the line it's paused on — somewhere, so it can resume later. That saved bundle is a stack frame, and they stack up on the call stack.
# In recursion they pile deep, because each call spawns another before any of them finish:
# dfs(root)            ← paused, waiting on...
#   dfs(root.left)     ← paused, waiting on...
#     dfs(root.left.left)     ← paused, waiting on...
#       dfs(None) → returns (0,0)   ← finally! the only one not waiting


### Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):

            # stopping condition of recursion for dfs (exploration of all houses)
            if node is None:
                return (0, 0)

            # recursion - the function calls itself
            L_rob, L_skip = dfs(node.left)
            R_rob, R_skip = dfs(node.right)

            rob_me = node.val + L_skip + R_skip
            skip_me = max(L_rob, L_skip) + max(R_rob, R_skip)

            return (rob_me, skip_me)

        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)
        


### Example
#   1
#  / \
# 2   3

# 1. call dfs(1)              stack: [1]
# 2.   1 calls dfs(2)         stack: [1, 2]
# 3.   2 is a leaf → returns (rob=2, skip=0)     stack: [1]
# 4.   1 calls dfs(3)         stack: [1, 3]
# 5.   3 is a leaf → returns (rob=3, skip=0)     stack: [1]
# 6.   1 now has both kids' pairs: left=(2,0), right=(3,0)
#         rob_me  = 1 + 0 + 0      = 1     (rob 1, kids must be skipped)
#         skip_me = max(2,0)+max(3,0) = 5  (skip 1, kids do their best)
#      returns (1, 5)         stack: []
# 7. answer = max(1, 5) = 5