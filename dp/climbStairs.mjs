class Solution {
	/**
	 * @param {number} n
	 * @return {number}
	 */
	climbStairs(n) {
		const seen = {};
		return this.#climb(n, seen);
	}

	#climb(n, seen) {
		if (n === 1) {
			return 1;
		}
		if (n === 2) {
			return 2;
		}
		if (seen[n] !== undefined) {
			return seen[n];
		}
		seen[n] = this.#climb(n - 1, seen) + this.#climb(n - 2, seen);
		return seen[n];
	}
}

const n = 3;
const sol = new Solution();
console.log(sol.climbStairs(n));
