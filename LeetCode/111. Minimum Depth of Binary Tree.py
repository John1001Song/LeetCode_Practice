# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # we need to find the shortest path, which means the leaf without children at the minimum depth 
        # we can do bfs and add 1 for each child node and until the child without nodes, then min func for the left and right child nodes 

        # corner case: no node
        if root == None:
            return 0

        # use queue to add node and its left and right children
        q = deque([(root, 1)])        # inite with a list, ele is tuple 
        while q:
            node, d = q.popleft() # get cur node and its height, FIFO
            if node == None: # when this node is a leaf, return its height without considering other longer branches
                return d
            # if node has children, append them into queue
            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))
        