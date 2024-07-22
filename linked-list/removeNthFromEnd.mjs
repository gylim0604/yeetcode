import { arrayToList, ListNode } from '../utils.mjs';

class Solution {
	/**
	 * @param {ListNode} head
	 * @param {number} n
	 * @return {ListNode}
	 */
	removeNthFromEnd(head, n) {
		const dummy = new ListNode(0, head);
		let fast = head;
		let slow = dummy;
		while (n > 0) {
			fast = fast.next;
			n--;
		}
		while (fast !== null) {
			slow = slow.next;
			fast = fast.next;
		}
		slow.next = slow.next.next;
		return dummy.next;
	}
}
// const head = arrayToList([1, 2, 3, 4]);
const head = arrayToList([1, 2]);
// const head = arrayToList([1, 2, 3, 4]);
const n = 2;
const sol = new Solution();
console.log(sol.removeNthFromEnd(head, n));
