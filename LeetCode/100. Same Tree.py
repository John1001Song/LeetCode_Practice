# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we need to compare two trees
        # we can compare the node.val first, then node.left, then node.right
        # if find difference, return false
        # if same, continue to next node. 
        # return true after the all the node checking

        # corner case: two trees are None
        if p == None and q == None:
            return True

        # corner case: one of them is None
        if p != None and q == None:
            return False
        else:
            if p == None and q != None:
                return False

        # normal case: two trees have nodes
        # def checkVal(p, q):
        #     if (p.val != q.val) or (p != None and q == None) or (p == None and q != None):
        #         return False
        #     return checkVal(p)
            
        # while p != None and q != None:
        #     if p.val != q.val:
        #         return False
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # corner case: one tree is finished, but the other is not
        # if p != None or q != None:
            # return False
        
        # normal case: two trees are finished checking
        # return True