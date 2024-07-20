import { createNode } from './utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} p
	 * @param {TreeNode} q
	 * @return {boolean}
	 */
	isSameTree(p, q) {
		if (!p && !q) return true;
		if (p && !q) return false;
		if (!p && q) return false;
		if (p?.value !== q?.value) return false;
		return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
	}
}

const p = createNode(1, createNode(2), createNode(3));
const q = createNode(1, createNode(3), createNode(2));
const sol = new Solution();
console.log(sol.isSameTree(p, q));
