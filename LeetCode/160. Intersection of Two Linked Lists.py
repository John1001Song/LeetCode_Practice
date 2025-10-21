# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # we need to find the intersected node and the skipA and skipB are not given. 
        # we need to return 0 if there is no intersection 

        # we take this method
        # from link A, pointer_A takes all steps until the end, then pointer_A starts from link B
        # from link B, pointer_B takes all steps until the end, the pointer_B starts from link A
        # the monemnt pointer_A meets pointer_B is the intersected node

        pointer_A = headA
        pointer_B = headB

        while pointer_A != pointer_B:
            # switch to the other link
            if pointer_A:
                pointer_A = pointer_A.next
            else:
                pointer_A = headB
            if pointer_B:
                pointer_B = pointer_B.next
            else:
                pointer_B = headA

        return pointer_A
