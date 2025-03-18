# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use BFS to compare values at cur node and its left and right
        # at the same time, we need to make sure that all the left branches are less than cur node and all the right branches are larger than current node 
        # thus we need to provide a valid range for current comparison
        # after each iteration, we need to update the valid range values
        def validate(node, low=float('-inf'), high=float('inf')):
            # edge case leaf
            if node == None:
                return True
            # cur node does not follow the rule
            if node.val <= low or node.val >= high:
                return False
            # recursive to left and right branches
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        # trigger the root
        return validate(root)