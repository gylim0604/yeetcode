class Solution {
	/**
	 * @param {number[]} cost
	 * @return {number}
	 */
	minCostClimbingStairs(cost) {
		return Math.min(this.#climb(cost, 0, 0, []), this.#climb(cost, 1, 0, []));
	}

	#climb(cost, idx, currCost, seen) {
		if (idx >= cost.length) {
			return currCost;
		}
		if (seen[idx]) return seen[idx];
		currCost += cost[idx] ?? 0;
		seen[idx] = Math.min(this.#climb(cost, idx + 1, currCost, seen), this.#climb(cost, idx + 2, currCost, seen));
		return seen[idx];
	}
}

const cost = [10, 15, 20];
const sol = new Solution();
console.log(sol.minCostClimbingStairs(cost));
