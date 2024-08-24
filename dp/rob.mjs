class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	rob(nums) {
		if (nums.length <= 2) {
			return Math.max(...nums);
		}
		for (let i = 2; i < nums.length; i++) {
			nums[i] += Math.max(nums[i - 2], nums[i - 3] || 0);
			// max = Math.max(max, nums[i]);
		}
		return Math.max(...nums);
	}
}

const nums = [2, 9, 1, 8, 3, 6];
const sol = new Solution();
console.log(sol.rob(nums));
