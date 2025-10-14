# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post order is left, right, then root
        
        # corner case: empty 
        if root == None:
            return []

        # normal case
        res = []
        def postOrder(node):
            if node == None:
                return
            if node.left:
                postOrder(node.left)
            if node.right:
                postOrder(node.right)
            res.append(node.val)
        
        postOrder(root)
        return res