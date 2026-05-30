/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        let fast=head;
        let slow=head;

        if(head===null){
            // A linked list with no item is having no cycle
            return false;
        }

        if(head.next===null){
            // A linked list with one node that points to null
            return false;
        }

        while(fast!==null && fast.next !=null){
            slow = slow.next;
            fast = fast.next.next;
            
            if(fast === slow){
                return true
            }
        }

        return false;
    }
}
