import { arrayToList } from '../utils.mjs';

class Solution {
	/**
	 * @param {number} stones
	 * @return {number}
	 */
	isPalindrome(head) {
		let dummy = head;
		let first = dummy;
		let second = this.#reverse(this.#getMid(head));

		while (second) {
			if (second.val !== first.val) return false;
			second = second.next;
			first = first.next;
		}
		return true;
	}

	#getMid(head) {
		let slow = head;
		let fast = head;
		while (fast) {
			slow = slow.next;
			fast = fast?.next?.next;
		}
		return slow;
	}

	#reverse(node) {
		let prev = null;
		let curr = node;
		while (curr) {
			const next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		return prev;
	}
}

const arr = [1, 2, 2, 1];
const head = arrayToList(arr);
const sol = new Solution();
console.log(sol.isPalindrome(head));
