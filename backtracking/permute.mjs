class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number[][]}
	 */
	permute(nums) {
		const res = [];
		const curr = [];
		const used = new Array(nums.length).fill(false);
		this.#singlePermuate(nums, res, curr, used);
		return res;
	}

	#singlePermuate(nums, res, curr, used) {
		if (curr.length === nums.length) {
			res.push([...curr]);
			return;
		}
		for (let i = 0; i < nums.length; i++) {
			if (used[i]) continue;
			curr.push(nums[i]);
			used[i] = true;
			this.#singlePermuate(nums, res, curr, used);
			curr.pop();
			used[i] = false;
		}
	}
}

const nums = [1, 2, 3];
const sol = new Solution();
console.log(sol.permute(nums));
