import { createNode } from './utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @param {TreeNode} subRoot
	 * @return {boolean}
	 */
	isSubtree(root, subRoot) {
		if (subRoot === null) return true;
		if (root === null) return false;
		if (this.isSameTree(root, subRoot)) return true;
		return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
	}

	isSameTree(p, q) {
		if (!p && !q) return true;
		if (p && !q) return false;
		if (!p && q) return false;
		if (p?.value !== q?.value) return false;
		return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
	}
}
const root = createNode(1);
const subRoot = createNode(0);

const sol = new Solution();
console.log(sol.isSubtree(root, subRoot));
