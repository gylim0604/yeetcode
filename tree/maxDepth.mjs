import { createNode } from './utils.mjs';

class Solution {
	/**
	 * @param {TreeNode} root
	 * @return {number}
	 */
	maxDepth(root) {
		this.iterativeDFS(root);
		this.recursiveDFS(root, 0);
	}

	iterativeDFS(root) {
		if (!root) return 0;
		const stack = [[root, 1]];
		let res = 1;
		while (stack.length > 0) {
			const [node, depth] = stack.shift();

			if (node) {
				console.log(node.value);
				res = Math.max(res, depth);
				stack.push([node.left, depth + 1]);
				stack.push([node.right, depth + 1]);
				console.log([...stack]);
			}
		}
		return res;
	}

	recursiveDFS(root, len) {
		if (root === null) return len;
		console.log(root.value);
		return Math.max(this.recursiveDFS(root.left, len + 1), this.recursiveDFS(root.right, len + 1));
	}

	bfs(root) {
		if (root === null) return 0;
		const queue = [root];
		let level = 0;
		while (queue.length > 0) {
			const curr = queue.shift();
			console.log(curr.value);

			if (curr.left) queue.push(curr.left);
			if (curr.right) queue.push(curr.right);
			level++;
		}
		return level;
	}
}

const sol = new Solution();
const root = createNode(3, createNode(9, createNode(11)), createNode(20, createNode(15), createNode(7)));

console.log(sol.maxDepth(root));
