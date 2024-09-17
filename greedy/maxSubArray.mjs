class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	maxSubArray(nums) {
		let [runningSum, maxSum] = [nums[0], nums[0]];
		for (let i = 1; i < nums.length; i++) {
			const num = nums[i];
			const sum = runningSum + num;
			runningSum = Math.max(num, sum);
			maxSum = Math.max(maxSum, runningSum);
		}
		return maxSum;
	}
}

const nums = [2, -3, 4, -2, 2, 1, -1, 4];
const sol = new Solution();
console.log(sol.maxSubArray(nums));
