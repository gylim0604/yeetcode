class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	rob(nums) {
		if (nums.length === 0) return 0;
		if (nums.length === 1) return nums[0];

		return Math.max(this.#robbing(nums.slice(0, -1)), this.#robbing(nums.slice(1)));
	}
	#robbing(nums) {
		let rob2 = 0;
		let rob1 = nums[0];
		for (let i = 1; i < nums.length; i++) {
			const current = Math.max(rob2 + nums[i], rob1);
			rob2 = rob1;
			rob1 = current;
		}
		return rob1;
	}
}

const nums = [2, 9, 8, 3, 6];
const sol = new Solution();
console.log(sol.rob(nums));
