class Solution {
	/**
	 * @param {number[]} cost
	 * @return {number}
	 */
	minCostClimbingStairs(cost) {
		return Math.min(this.#climb(cost, 0, 0), this.#climb(cost, 1, 0));
	}

	#climb(cost, idx, currCost) {
		if (idx >= cost.length) {
			return currCost;
		}
		currCost += cost[idx] ?? 0;
		const cost1 = this.#climb(cost, idx + 1, currCost);
		const cost2 = this.#climb(cost, idx + 2, currCost);
		return Math.min(cost1, cost2);
	}
}

const cost = [10, 15, 20];
const sol = new Solution();
console.log(sol.minCostClimbingStairs(cost));
