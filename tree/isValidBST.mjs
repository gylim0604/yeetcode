import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {boolean}
	 */
	isValidBST(root) {
		if (root === null) return true;
		return this.helper(root, -Infinity, Infinity);
	}
	helper(node, min, max) {
		if (node === null) return true;
		if (node.val <= min || node.val >= max) return false;
		return this.helper(node.left, min, node.val) && this.helper(node.right, node.val, max);
	}
}

const root = arrayToBinaryTree([2, 1, 3]);
const sol = new Solution();
console.log(sol.isValidBST(root));
