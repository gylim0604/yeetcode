class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	jump(nums) {
		return this.#greedy(nums);
		// return this.#dp(nums, 0, 0);
	}

	#dp(nums, index, count) {
		if (index >= nums.length - 1) {
			return 0;
		}

		let minSteps = Infinity;

		for (let i = nums[index]; i > 0; i--) {
			const steps = this.#dp(nums, index + i, count + 1);
			minSteps = Math.min(steps + 1, minSteps);
		}
		return minSteps;
	}

	#greedy(nums) {
		let res = 0;
		let l = 0,
			r = 0;

		while (r < nums.length - 1) {
			let farthest = 0;
			for (let i = l; i < r + 1; i++) {
				farthest = Math.max(farthest, i + nums[i]);
			}
			l = r + 1;
			r = farthest;
			res++;
		}
		return res;
	}
}

const nums = [2, 1, 2, 1, 0];
const sol = new Solution();
console.log(sol.jump(nums));
