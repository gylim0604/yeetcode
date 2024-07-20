import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number[][]}
	 */
	levelOrder(root) {
		if (root === null) return [];
		let queue = [root];
		const res = new Array();
		while (queue.length > 0) {
			// handle current level
			const val = [];
			const len = queue.length;
			for (let i = 0; i < len; i++) {
				const curr = queue.shift();
				val.push(curr.val);
				if (curr.left) {
					queue.push(curr.left);
				}
				if (curr.right) {
					queue.push(curr.right);
				}
			}
			res.push(val);
		}
		return res;
	}
}

const root = arrayToBinaryTree([1, 2, 3, 4, 5, 6, 7]);
const sol = new Solution();
console.log(sol.levelOrder(root));
