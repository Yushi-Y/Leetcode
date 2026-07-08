# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]

#     2
#    / \
#   1   3

# Output: true
# Example 2:
# Input: root = [5,1,4,null,null,3,6]

#      4
#    /  \
#   1    6
#  / \  / \
# 0  2 5   7

# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# Constraints:

# The number of nodes in the tree is in the range [1, 10⁴].
# -2³¹ <= Node.val <= 2³¹ - 1


### Thoughts
# 递归判断每个节点node，left subtree的所有node < 当前node < right subtree的所有node
# this is equivalent to: 递归往下传导时，判断/记录每个node可取到的min 和 max value，判断node 的值在不在（min，max）范围内
# 如果有任何node不满足这个条件，return false

# summary: 递归判断每个node是否落在合理的区间内，然后recusivelycheck左右的subtrees

### TC：O(n) - n is the number of nodes.
# Every node is visited exactly once, and the work per node (bounds comparison, two recursive calls) is O(1). No node is ever revisited
### SC: O(h) where h is tree height — that's the recursion stack depth. 
# No other data structures are used; the bounds are just two values passed per frame.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, node, min_val, max_val):
        if not node: # empty node is fine - an empty subtree can't violate anything/fall outside bounds
            return True

        # condition: check node val within (min, max)
        if not min_val < node.val < max_val:
            return False
        
        # check left and right subtrees recursively on this condition
        return self.helper(node.left, min_val, node.val) and self.helper(node.right, node.val, max_val)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

