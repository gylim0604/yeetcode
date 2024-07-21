import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number}
	 */
	goodNodes(root) {
		if (root === null) return 0;
		return this.countGoodNodes(root, root.val);
	}
	countGoodNodes(node, max) {
		if (node === null) return 0;

		const currMax = Math.max(max, node.val);
		return (node.val >= max ? 1 : 0) + this.countGoodNodes(node.left, currMax) + this.countGoodNodes(node.right, currMax);
	}

	getGoodNodes(node, max) {
		if (node === null) return [];

		const currMax = Math.max(max, node.val);
		return [...(node.val >= max ? [node.val] : []), ...this.getGoodNodes(node.left, currMax), ...this.getGoodNodes(node.right, currMax)];
	}
}

const root = arrayToBinaryTree([1, 2, -1, 3, 4]);
const sol = new Solution();
console.log(sol.goodNodes(root));
