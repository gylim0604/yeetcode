import { arrayToList } from '../utils.mjs';

class Solution {
	/**
	 * @param {ListNode} head
	 * @return {ListNode}
	 */
	reverseList(head) {
		let prev = null;
		let curr = head;
		while (curr) {
			const next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		return prev;
	}
}

const list = arrayToList([0, 1, 2, 3]);
const sol = new Solution();
console.log(sol.reverseList(list));
