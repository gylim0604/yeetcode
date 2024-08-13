class Solution {
	/**
	 * @param {number[]} nums
	 * @param {number} target
	 * @returns {number[][]}
	 */
	combinationSum(nums, target) {
		const res = [];
		const cur = [];
		this.#singleCombination(nums, target, res, cur, 0);
		return res;
	}

	#singleCombination(nums, target, res, cur, index) {
		if (target === 0) {
			res.push([...cur]);
		} else if (target < 0 || index >= nums.length) {
			return;
		} else {
			cur.push(nums[index]);
			this.#singleCombination(nums, target - nums[index], res, cur, index);
			cur.pop();
			this.#singleCombination(nums, target, res, cur, index + 1);
		}
	}
}

const nums = [2, 5, 6, 9],
	target = 9;
const sol = new Solution();
console.log(sol.combinationSum(nums, target));
