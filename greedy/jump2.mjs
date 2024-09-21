class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	jump(nums) {
		return this.#explore(nums, 0, 0);
	}

	#explore(nums, index, count) {
		if (index >= nums.length - 1) {
			return 0;
		}

		let minSteps = Infinity;

		for (let i = nums[index]; i > 0; i--) {
			const steps = this.#explore(nums, index + i, count + 1);
			minSteps = Math.min(steps + 1, minSteps);
		}
		return minSteps;
	}
}

const nums = [2, 1, 2, 1, 0];
const sol = new Solution();
console.log(sol.jump(nums));
