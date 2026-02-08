# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left  # Left child (another TreeNode or None)
#         self.right = right  # Right child (another TreeNode or None)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)

        return max(left_length, right_length) + 1
        