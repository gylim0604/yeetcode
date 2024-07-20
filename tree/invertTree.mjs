import { createNode } from './utils.mjs';

const tree = createNode(1, createNode(2, createNode(4, createNode(5, createNode(11, createNode(12))))), createNode(3, createNode(6), createNode(7)));
// console.log(tree);

function dfs(root) {
	if (!root) return root;
	const stack = [root];

	while (stack.length > 0) {
		const curr = stack.pop();
		const temp = curr.right;
		curr.right = curr.left;
		curr.left = temp;
		if (curr.right) stack.push(curr.right);
		if (curr.left) stack.push(curr.left);
	}
	return root;
}

console.log(dfs(tree));
