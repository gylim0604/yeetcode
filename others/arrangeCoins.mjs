class Solution {
	/**
	 * @param {number[]} n
	 * @return {number}
	 */
	arrange(n) {
		let l = 1,
			r = n;
		let res = 0;
		while (l <= r) {
			const mid = Math.floor((l + r) / 2);
			const coins = (mid / 2) * (mid + 1);
			if (coins > n) {
				r = mid - 1;
			} else {
				l = mid + 1;
				res = Math.max(mid, res);
			}
		}
		return res;
	}
}

const n = 7;
const sol = new Solution();
console.log(sol.arrange(n));
