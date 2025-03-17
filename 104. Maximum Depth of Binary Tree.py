# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS 
    # run down from left, until the leaf, then right
    # compare the this depth with the other depth, keep the longer one
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # no need to construct tree based on inupt 
        # base case: reach root
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left, right)
        