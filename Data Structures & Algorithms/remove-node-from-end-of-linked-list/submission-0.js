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
    findLength(head) {
        let n = 0;
        while (head !== null) {
            n++;
            head = head.next;
        }

        return n;
    }
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let len = this.findLength(head);

        let target = len - n;

        if (target === 0) {
            return head.next;
        }

        let curr = head;

        for (let i = 1; i < target; i++) {
            curr = curr.next;
        }

        curr.next = curr.next.next;

        return head;
    }
}
