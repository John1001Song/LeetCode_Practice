/**
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

// solution from LeetCode

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        dummyHead = new ListNode(0);
        carry = 0;
        
        ListNode p = l1, q = l2, currDigt = dummyHead;
        
        while(p1 != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            
            currDigt.next = new ListNode(sum%10);
            currDigt = currDigt.next;

            if (p != null) {
            	p = p.next;
            }
            if (q != null) {
            	q = q.next;
            }
        }
        
        if (carry > 0) {
        	currDigt = new ListNode(carry);
        }

        return dummyHead.next;
    }
}