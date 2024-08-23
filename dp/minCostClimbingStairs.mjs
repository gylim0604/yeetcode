class Solution {
	/**
	 * @param {number[]} cost
	 * @return {number}
	 */
	minCostClimbingStairs(cost) {
		cost.push(0);
		for (let i = cost.length - 3; i >= 0; i--) {
			console.log(cost[i]);
			cost[i] = Math.min(cost[i + 1], cost[i + 2]) + cost[i];
		}
		return Math.min(cost[0], cost[1]);
	}
}

const cost = [10, 15, 20];
const sol = new Solution();
console.log(sol.minCostClimbingStairs(cost));
