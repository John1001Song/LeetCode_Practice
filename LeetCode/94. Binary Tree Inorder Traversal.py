# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # this question changes a tree from pre-order to in-order 
        def in_order(node):
            # base case:
            if node == None:
                return []

            return in_order(node.left) + [node.val] + in_order(node.right)
        
        
        return in_order(root)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # this question changes a tree from pre-order to in-order 
        res = []
        def in_order(node):
            # base case:
            if node is None:
                return
            in_order(node.left)
            res.append(node.val)
            in_order(node.right)
        
        
        in_order(root)
        return res