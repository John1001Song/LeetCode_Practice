# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # The question wants to determine if the linked list is looped/cycle, and input does not have pos parameter
        # assume all nodes are unique 
        # naive approach is to add all nodes into a set, if the next node is in the set, then we find a loop/cycle 

        # corner case: empty head
        if head == None:
            return False
        # corner case: head only
        if head.next == None:
            return False
        
        # normal cases
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
                head = head.next
        
        return False