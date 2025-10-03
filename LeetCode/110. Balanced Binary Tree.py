# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # as long as left and right banches height diff is <= 1, then they are height balanced
        # 
        # corner case: empty tree
        if root == None:
            return True

        def dfs(node):
            # base case: on leave level, height add on 0
            if node == None:
                return True, 0
            
            # left branch
            left_balanced, left_height = dfs(node.left)
            # un balanced found, return False
            if left_balanced == False:
                return False, 0
            
            # right branch
            right_balanced, right_height = dfs(node.right)
            if right_balanced == False:
                return False, 0

            if abs(left_height - right_height) > 1:
                return False, 0
            else:
                return True, 1 + max(left_height, right_height)

        return dfs(root)[0]