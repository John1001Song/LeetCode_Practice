# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we compare two nodes and attach the smaller one, leave the larger one for the next comparison
        # when one linked list got tail, we attach the unfinished one to the result list tail.
        
        res = ListNode(None, None) # head to keep nodes after comparisons
        cur = res # initially, cur is same as result node, and result node stays there 

        # corner case: one list is empty, just return the other 
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        while list1 != None and list2 != None:
            if list1.val <= list2.val: # list 1 node has a smaller one
                cur.next = list1 # attach this smaller node to cur node list
                list1 = list1.next # shift list 1 to next node 
                cur = cur.next # move cur (pointer) to its next and ready for new smaller node 
            else: # list 2 node has a smaller one 
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        
        # when one of the lists is empty, attach the non empty list to cur node 
        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2
        
        return res.next # res has a dummy head node, so we return the next node 
