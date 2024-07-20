import { arrayToList, ListNode } from '../utils.mjs';

class Solution {
	/**
	 * @param {ListNode} l1
	 * @param {ListNode} l2
	 * @return {ListNode}
	 */
	addTwoNumbers(l1, l2) {
		let head1 = l1;
		let head2 = l2;
		let leftover = false;
		const res = new ListNode();
		let curr = res;

		while (head1 || head2) {
			// To handle case where there is flowover;
			let val = (head1?.val ?? 0) + (head2?.val ?? 0) + leftover;
			if (val >= 10) {
				val = val % 10;
				leftover = true;
			} else {
				leftover = false;
			}
			curr.next = new ListNode(val);
			head1 = head1?.next;
			head2 = head2?.next;
			curr = curr.next;
		}
		if (leftover) {
			curr.next = new ListNode(1);
		}
		return res.next;
	}
}

const l1 = arrayToList([9, 9, 9, 9, 9, 9, 9]),
	l2 = arrayToList([9, 9, 9, 9]);

const sol = new Solution();
console.log(sol.addTwoNumbers(l1, l2));
