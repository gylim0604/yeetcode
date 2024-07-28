import { arrayToBinaryTree } from '../utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @param {number} k
	 * @return {number}
	 */
	kthSmallest(root, k) {
		const context = { k: k, res: null };
		this.#inOrder(root, context);
		return context.res;
	}
	#inOrder(root, context) {
		// traverse till you get the smallest one
		// once the smallest is found, start counting back
		debugger;
		if (root === null) {
			return;
		}
		this.#inOrder(root.left, context);
		context.k -= 1;
		if (context.k === 0) {
			context.res = root.val;
			return;
		}
		this.#inOrder(root.right, context);
	}
}

const root = arrayToBinaryTree([4, 3, 5, 2, null]);
const k = 2;
const sol = new Solution();
console.log('Results...', sol.kthSmallest(root, k));
