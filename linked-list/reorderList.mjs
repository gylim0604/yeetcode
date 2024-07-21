import { arrayToList } from '../utils.mjs';

class Solution {
	/**
	 * @param {ListNode} head
	 * @return {void}
	 */
	reorderList(head) {
		let dummy = head;
		let curr = dummy;
		//find the middle point and reverse it
		// This part is O(n) + O(n)
		let reversed = this.reverse(this.getMid(head));
		// merge reversed part into actual
		// actual merging again takes O(n)
		while (reversed) {
			const nextEl = reversed;
			reversed = reversed.next;
			nextEl.next = curr.next;
			curr.next = nextEl;
			curr = curr.next.next;
		}
		curr.next = null;
		// Final time complexity is O(n) + O(n) + O(n) = O(3n) ~ O(n)
		return dummy;
	}

	// O(n/2) = O(n)
	getMid(head) {
		let slow = head;
		let fast = head;
		while (fast) {
			slow = slow.next;
			fast = fast?.next?.next;
		}
		return slow;
	}

	// O(n)
	reverse(head) {
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

const root = arrayToList([0, 1, 2, 3, 4, 5, 6]);
const sol = new Solution();
const res = sol.reorderList(root);
console.log(res);
