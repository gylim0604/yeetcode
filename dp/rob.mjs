class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	rob(nums) {
		if (nums.length === 0) return 0;
		if (nums.length === 1) return nums[0];

		let prev2 = 0; // max profit for robbing previous 2 houses
		let prev1 = nums[0]; // max profit of robbing previous house
		for (let i = 1; i < nums.length; i++) {
			const current = Math.max(prev2 + nums[i], prev1);
			prev2 = prev1;
			prev1 = current;
		}
		return prev1;
	}
}

const nums = [2, 9, 1, 8, 3, 6];
const sol = new Solution();
console.log(sol.rob(nums));
