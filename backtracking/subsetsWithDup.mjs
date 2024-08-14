class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number[][]}
	 */
	subsetsWithDup(nums) {
		const res = [];
		const curr = [];
		nums.sort((a, b) => a - b);
		this.#singleSubset(nums, res, curr, 0);
		return res;
	}

	#singleSubset(nums, res, curr, index) {
		if (index > nums.length) {
			return;
		}
		res.push([...curr]);
		for (let i = index; i < nums.length; i++) {
			if (i > index && nums[i] === nums[i - 1]) continue;
			curr.push(nums[i]);
			this.#singleSubset(nums, res, curr, i + 1);
			curr.pop();
		}
	}
}

const nums = [1, 2, 1];

// const nums = [7, 7];
const sol = new Solution();
console.log(sol.subsetsWithDup(nums));
