# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # the question is about to find a sum from root to leaf and sum is equal to the targetSum. 
        # one of the approach can be DFS, go deaper and find leaf first, if equal to sum, return true, else, go to parent node and go to sibling node 

        # corner case: no root 
        if root == None:
            return False

        # corner case: if one root node 
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True
            else:
                return False

        def dfs(node, remain):
            # empty node 
            if node == None:
                return False
            # leaf node 
            if node.left == None and node.right == None:
                if (remain - node.val) == 0:
                    return True
                else:
                    return False
            # branch node 
            new_remain = remain - node.val
            return dfs(node.left, new_remain) or dfs(node.right, new_remain)
        
        return dfs(root, targetSum)