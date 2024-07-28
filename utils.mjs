export function createNode(value, left = null, right = null) {
	return { value, left, right };
}

export class ListNode {
	constructor(value = null, next = null) {
		this.val = value;
		this.next = next;
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

export class MinHeap {
	constructor() {
		this.heap = [];
	}
	#getParent(index) {
		return Math.floor((index - 1) / 2);
	}
	#getLeftChild(index) {
		return 2 * index + 1;
	}
	#getRightChild(index) {
		return 2 * index + 2;
	}

	#swap(index1, index2) {
		[this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]];
	}

	insert(value) {
		this.heap.push(value);
		this.#bubbleUp();
	}
	#bubbleUp() {
		let index = this.heap.length - 1;
		while (index > 0) {
			let parentIndex = this.#getParent(index);
			if (this.heap[parentIndex] > this.heap[index]) {
				this.#swap(parentIndex, index);
				index = parentIndex;
			} else {
				break;
			}
		}
	}

	remove() {
		if (this.heap.length === 0) return null;
		if (this.heap.length === 1) return this.heap.pop();

		const root = this.heap[0];
		this.heap[0] = this.heap.pop();
		this.#bubbleDown();
		return root;
	}
	#bubbleDown() {
		let index = 0;
		const length = this.heap.length;
		const el = this.heap[0];

		while (true) {
			let leftIndex = this.#getLeftChild(index);
			let rightIndex = this.#getRightChild(index);
			let leftChild, rightChild;
			let swapIndex = null;

			if (leftIndex < length) {
				leftChild = this.heap[leftIndex];
				if (leftChild < el) {
					swapIndex = leftIndex;
				}
			}

			if (rightIndex < length) {
				rightChild = this.heap[rightIndex];
				if ((swapIndex !== null && rightChild < leftChild) || (swapIndex === null && rightChild < el)) {
					swapIndex = rightIndex;
				}
			}

			if (swapIndex === null) break;

			this.#swap(index, swapIndex);
			index = swapIndex;
		}
	}

	peek() {
		if (this.heap.length === 0) return null;
		return this.heap[0];
	}

	size() {
		return this.heap.length;
	}
}

export class MaxHeap {
	constructor() {
		this.heap = [];
	}
	#getParent(index) {
		return Math.floor((index - 1) / 2);
	}
	#getLeftChild(index) {
		return 2 * index + 1;
	}
	#getRightChild(index) {
		return 2 * index + 2;
	}

	#swap(index1, index2) {
		[this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]];
	}

	insert(value) {
		this.heap.push(value);
		this.#bubbleUp();
	}
	#bubbleUp() {
		let index = this.heap.length - 1;
		while (index > 0) {
			let parentIndex = this.#getParent(index);
			if (this.heap[parentIndex] < this.heap[index]) {
				this.#swap(parentIndex, index);
				index = parentIndex;
			} else {
				break;
			}
		}
	}

	remove() {
		if (this.heap.length === 0) return null;
		if (this.heap.length === 1) return this.heap.pop();

		const root = this.heap[0];
		this.heap[0] = this.heap.pop();
		this.#bubbleDown();
		return root;
	}
	#bubbleDown() {
		let index = 0;
		const length = this.heap.length;
		const el = this.heap[0];

		while (true) {
			let leftIndex = this.#getLeftChild(index);
			let rightIndex = this.#getRightChild(index);
			let leftChild, rightChild;
			let swapIndex = null;

			if (leftIndex < length) {
				leftChild = this.heap[leftIndex];
				if (leftChild > el) {
					swapIndex = leftIndex;
				}
			}

			if (rightIndex < length) {
				rightChild = this.heap[rightIndex];
				if ((swapIndex !== null && rightChild > leftChild) || (swapIndex === null && rightChild > el)) {
					swapIndex = rightIndex;
				}
			}

			if (swapIndex === null) break;

			this.#swap(index, swapIndex);
			index = swapIndex;
		}
	}

	peek() {
		if (this.heap.length === 0) return null;
		return this.heap[0];
	}

	size() {
		return this.heap.length;
	}
}
