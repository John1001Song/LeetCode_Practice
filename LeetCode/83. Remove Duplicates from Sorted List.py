# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the question wants to remove duplicated elements and we can check cur node's neighbors until its next neighbor is different 
        cur = head
        # corner case: the given list is empty
        if cur == None:
            return None
        
        # normal case: the list contains multple nodes
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
