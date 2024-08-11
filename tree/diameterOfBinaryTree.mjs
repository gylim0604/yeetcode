import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number}
	 */
	diameterOfBinaryTree(root) {
		let res = 0;
		const depth = (node) => {
			if (node === null) return 0;
			const leftDepth = depth(node.left);
			const rightDepth = depth(node.right);

			res = Math.max(res, leftDepth + rightDepth);
			return Math.max(leftDepth, rightDepth) + 1;
		};
		depth(root);
		return res;
	}
}

const arr = [1, null, 2, 3, 4, 5];
const root = arrayToBinaryTree(arr);

const sol = new Solution();
console.log(sol.diameterOfBinaryTree(root));
