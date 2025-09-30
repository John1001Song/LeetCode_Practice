# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # we need to find the symmetric nodes in the tree
        # it means node.left == node.right 
        # the root node is the center line of symmetric
        # node.left.val == node.right.val 

        # corner case: root only
        if root.left == None and root.right == None:
            return True
        
        # corner case: one of the side is None and the other is not
        if root.left == None or root.right == None:
            return False
        
        def isMirror(a, b):
            # case: both are None
            if a == None and b == None:
                return True
            elif a == None or b == None: # One of them is None
                return False
            else: # both have values
                if a.val != b.val:
                    return False
                else: # both vals are same, check for its nodes
                    return isMirror(a.left, b.right) and isMirror(a.right, b.left)
                
        return isMirror(root.left, root.right)
        
