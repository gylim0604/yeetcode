import { createNode } from './utils.mjs';
class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number}
	 */
	isBalanced(root) {
		if (!root) return true;
		return this.checkBalance(root).balanced;
	}

	checkBalance(node) {
		if (node === null) return { height: 0, balanced: true };
		const left = this.checkBalance(node.left);
		const right = this.checkBalance(node.right);

		const height = 1 + Math.max(left.height, right.height);
		const balanced = left.balanced && right.balanced && Math.abs(left.height - right.height) <= 1;

		return { height, balanced };
	}
}

const root = createNode(1, createNode(2, createNode(3, createNode(4), createNode(4)), createNode(3)), createNode(2));
const sol = new Solution();
console.log(sol.isBalanced(root));
