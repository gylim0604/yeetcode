import { MaxHeap } from '../utils.mjs';

class Solution {
	/**
	 * @param {*} stones
	 * @returns {number}
	 */
	lastStoneWeight(stones) {
		while (stones.length > 1) {
			const len = stones.length - 1;
			stones.sort((a, b) => a - b);
			stones[len - 1] = stones[len] - stones[len - 1];
			stones.pop();
		}
		if (stones[0] === 0) return 0;
		return stones.pop();
	}

	lastStoneWeightHeap(stones) {
		const heap = new MaxHeap();
		stones.map((el) => heap.insert(el));
		while (heap.size() > 1) {
			const first = heap.remove();
			const second = heap.remove();
			const remainder = first - second;
			if (remainder > 0) {
				heap.insert(remainder);
			}
		}
		return heap.remove() ?? 0;
	}
}

const stones = [2, 2];
const sol = new Solution();
console.log(sol.lastStoneWeightHeap(stones));
