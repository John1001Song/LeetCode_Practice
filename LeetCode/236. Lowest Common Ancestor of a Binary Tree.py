# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # do DFS to check all nodes
        
        # edge case (base case) this node is None or p or q
        # return this node 
        if root == None or root == p or root == q:
            return root
        
        # when this node is a joint node, and not p and not q,
        # recursive to call this func: one goes to left branch and the other goes to right 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # when receive the returned nodes from left and right, which could be None, p or q
        # due to if returned is p or q, it will return to upper level function 
        # so we can have a logic and combination here for left and right 
        # if both left and right meet p and q, then we can immediately return this node, which is the lowest common ancestor 
        if left and right:
            return root

        # return the non None branch
        if left != None:
            return left
        else:
            return right