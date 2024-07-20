import { arrayToBinaryTree } from '../utils.mjs';
class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number[][]}
	 */
	levelOrder(root) {
		if (root === null) return [];
		let stack = [root];
		const res = new Array();
		let temp = new Array();
		let currArr = [];
		while (stack.length > 0) {
			// handle current level
			const curr = stack.shift();
			currArr.push(curr.val);
			// handle children
			if (curr.left) temp.push(curr.left);
			if (curr.right) temp.push(curr.right);
			//  current level is done
			if (stack.length === 0) {
				stack = [...temp];
				temp = [];
				res.push(currArr);
				currArr = [];
				console.log(res);
			}
		}
		return res;
	}
}

const root = arrayToBinaryTree([1, 2, 3, 4, 5, 6, 7]);
const sol = new Solution();
console.log(sol.levelOrder(root));
