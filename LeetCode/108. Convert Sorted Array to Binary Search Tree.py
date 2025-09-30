# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # the question wants a balanced tree and it should be bineary search tree, where left < cur < right
        # given nums list is a stricktly increaing order, so left ele < right ele
        # the left ele could be placed from top 
        # we need to build the tree 

        # corner case: one element
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # normal case: build the tree
        # since nums is increasing, the middle ele can be the root, left tree is the left list, right tree is the right list 
        # we can iterate this process until the last element 
        def buildTree(left, right):
            if left > right:
                return None # no node built
            # middle index
            middle = (left + right) // 2
            cur_root = TreeNode(nums[middle])
            cur_root.left = buildTree(left, middle-1)
            cur_root.right = buildTree(middle+1, right) 

            return cur_root

        return buildTree(0, len(nums)-1)