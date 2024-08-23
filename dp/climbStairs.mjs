class Solution {
	/**
	 * @param {number} n
	 * @return {number}
	 */
	climbStairs(n) {
		// using array solution
		// const seen = {};
		// return this.#climb(n, seen);
		return this.#climbNoArr(n);
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

	#climbNoArr(n) {
		if (n <= 3) return n;
		let n1 = 2;
		let n2 = 3;
		for (let i = 4; i <= n; i++) {
			let temp = n1 + n2;
			n1 = n2;
			n2 = temp;
		}
		return n2;
	}
}

const n = 5;
const sol = new Solution();
console.log(sol.climbStairs(n));
