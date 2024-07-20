export function createNode(value, left = null, right = null) {
	return { value, left, right };
}

export class ListNode {
	constructor(value = null) {
		this.val = value;
		this.next = null;
	}
}

export function arrayToList(arr) {
	if (arr.length === 0) return null;

	const head = new ListNode(arr[0]);
	let curr = head;

	for (let i = 1; i < arr.length; i++) {
		const newNode = new ListNode(arr[i]);
		curr.next = newNode;
		curr = newNode;
	}
	return head;
}

export class TreeNode {
	constructor(value = null) {
		this.val = value;
		this.left = null;
		this.right = null;
	}
}

function constructTree(arr, index) {
	if (index >= arr.length || arr[index] === null) return null;

	const node = new TreeNode(arr[index]);
	node.left = constructTree(arr, 2 * index + 1);
	node.right = constructTree(arr, 2 * index + 2);

	return node;
}

export function arrayToBinaryTree(arr) {
	return constructTree(arr, 0);
}
