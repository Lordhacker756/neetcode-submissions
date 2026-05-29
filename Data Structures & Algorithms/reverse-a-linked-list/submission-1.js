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
     * @return {ListNode}
     */
    reverseList(head) {
        console.log(head)
        if(head==null || head.next ==null){
            return head
        }

        let prev = null;

        while(head.next !=null){
            let temp = head.next;

            head.next = prev;
            prev = head;

            head = temp;
        }

        head.next=prev

        return head;
    }
}
