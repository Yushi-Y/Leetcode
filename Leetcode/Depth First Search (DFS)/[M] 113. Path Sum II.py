### Thoughts - DFS + backtracking
# Walk down from the root, tracking the running sum (or the remaining amount).
# A path counts only if you're at a leaf (both children null) and the sum matches — not just any node where it matches.
# Append before recursing, pop after, so siblings start from a clean state.

# The rule of thumb: BFS earns its keep when you care about levels or shortest path in a tree. Here you want complete root-to-leaf paths, and DFS's stack mirrors a path naturally — so DFS is the clean choice.


### TC - n is number of nodes
# TC: traverse the tree O(n), copy the path to output is max O(n^2) = O(n^2)
# SC: recursion O(n), path save O(n) = O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = [] # all good paths
        path = [] # current path for backtracking

        def dfs(node, remaining):
            # edge case
            if node is None:
                return
            
            path.append(node.val)
            remaining = remaining - node.val # remaining sum 

            if node.left is None and node.right is None and remaining == 0: # end of path, also exact sum we need
                output.append(path.copy())

            dfs(node.left, remaining)
            dfs(node.right, remaining)

            path.pop() # backtrack, pop the last element

        
        dfs(root, targetSum)

        return output

