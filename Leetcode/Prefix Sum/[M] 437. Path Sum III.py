# The essense is prefix sum + hashmap look up, like Q560. 
# But for trees, prefix sum calculation is not straightforward as in arrays. So we use DFS to construct the workable paths and compute prefix sums, then added to the hashmap
# DFS steps:
# Extends the prefix sum by adding the current node's value
# Checks the hashmap for valid paths (same as the array problem)
# Recurses into left and right children, then backtracks so sibling branches don't see each other's prefix sums

# Time: O(n) — visit each node once with O(1) hashmap work.
# Space: O(n) — hashmap + recursion stack (O(n) in worst case for a skewed tree, O(log n) for balanced).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        seen = {0: 1} # empty tree has no value

        
        def dfs(node, prefix_sum):
            nonlocal count # I'm not creating a new count — I mean the count from the outer function
            if not node:
                return

            prefix_sum += node.val
            count += seen.get(prefix_sum - targetSum, 0)
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)

            # Backtrack: remove this node's prefix sum before returning
            seen[prefix_sum] -= 1
            # Why backtrack? Without it, a prefix sum from one branch would "leak" into a sibling branch, giving false matches. Each root-to-node path must be independent.


        dfs(root, 0) # start with first node, with zero sum
        return count



### Why backtrack example:
#         1
#        / \
#       2   2
# targetSum = 3
# With backtracking (correct):

# Visit 1: prefix_sum = 1, seen = {0:1, 1:1}
# Visit left 2: prefix_sum = 3, look up 3-3=0 → found 1 match ✅, seen = {0:1, 1:1, 3:1}
# Backtrack: seen = {0:1, 1:1, 3:0}
# Visit right 2: prefix_sum = 3, look up 3-3=0 → found 1 match ✅

# Answer: 2 (path 1→2 on each side). Correct!

# Without backtracking (leaked):

# Visit 1: prefix_sum = 1, seen = {0:1, 1:1}
# Visit left 2: prefix_sum = 3, look up 3-3=0 → found 1 match ✅, seen = {0:1, 1:1, 3:1}
# No backtrack, 3 stays in the map
# Visit right 2: prefix_sum = 3, look up 3-3=0 → found 1 match ✅, but also seen has 3:1 from the left branch...

# Now if targetSum = 0, at the right 2 you'd look up 3-0=3, find it in the map from the left branch, and count a fake path that jumps across branches (left 2 → right 2), which isn't a valid downward path.
# That's the leak — the left branch's prefix sum pollutes the right branch's lookups.


        