class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	jump(nums) {
		let furthest = 0;

		for (let i = 0; i < nums.length; i++) {
			if (i > furthest) return false;
			furthest = Math.max(furthest, i + nums[i]);
			if (furthest >= nums.length - 1) {
				return true;
			}
		}
		return false;
	}
}

const nums = [2, 3, 1, 1, 4];
const sol = new Solution();
console.log(sol.jump(nums));
