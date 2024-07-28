class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number[][]}
	 */
	subsets(nums) {
		const res = [];
		this.#backtrack(nums, 0, [], res);
		return res;
	}

	#backtrack(nums, i, subset, res) {
		// add current
		if (i >= nums.length) {
			res.push([...subset]);
			return;
		}
		subset.push(nums[i]);
		this.#backtrack(nums, i + 1, subset, res);
		subset.pop();
		this.#backtrack(nums, i + 1, subset, res);
	}
}

const sol = new Solution();
debugger;
console.log(sol.subsets([1, 2, 3]));
