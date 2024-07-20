import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number[]}
	 */
	rightSideView(root) {
		if (root === null) return [];
		let queue = [root];

		const res = new Array();

		while (queue.length > 0) {
			const len = queue.length;

			for (let i = 0; i < len; i++) {
				const curr = queue.shift();
				if (i === len - 1) res.push(curr.val);
				if (curr.left) queue.push(curr.left);
				if (curr.right) queue.push(curr.right);
			}
		}
		return res;
	}
}

const root = arrayToBinaryTree([1, 2, 3, null, 5, 6, null, null, null, 4]);

const sol = new Solution();
console.log(sol.rightSideView(root));
