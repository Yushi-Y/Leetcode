# Hint 1 – Recursion on Trees
# This is a natural recursion problem. At each node, you have a value and two children. How does the remaining target change as you go deeper?
# Hint 2 – Shrinking the Target
# Instead of tracking a running sum, think about subtracting the current node's value from targetSum as you recurse down. What should targetSum equal when you reach a leaf for the path to be valid?
# Hint 3 – What is a Leaf?
# A leaf has no left child AND no right child. This is your base case. Be careful — a node with only one child is NOT a leaf.
# Hint 4 – The Recurrence
# At each node, the path sum exists if:
# The left subtree has a path summing to targetSum - node.val, OR
# The right subtree has a path summing to targetSum - node.val
# Hint 5 – Edge Case
# What should you return if root is None? Think about why returning False makes sense here.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        
        if not root.left and not root.right: # so a leaf node
            return targetSum == 0

        # recurse: does either subtree have a valid path?
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        