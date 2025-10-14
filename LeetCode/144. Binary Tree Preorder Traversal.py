# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # this question wants to print out all nodes in the order of root, left, then right 
        # we can use recursive func to do it 

        # corner case: no tree
        if root == None:
            return []

        res_list = []
        def preOrder(node):
            if node == None:
                return None
            else:
                res_list.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return res_list

# solution 2: stack LIFO
        if not root:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res