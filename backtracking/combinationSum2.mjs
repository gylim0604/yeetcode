class Solution {
	/**
	 * @param {number[]} candidates
	 * @param {number} target
	 * @return {number[][]}
	 */
	combinationSum2(candidates, target) {
		const res = [];
		const curr = [];
		const seen = new Array(candidates.length).fill(false);
		candidates.sort((a, b) => a - b);
		this.#singleCombination(candidates, target, res, curr, 0, seen);
		return res;
	}

	#singleCombination(nums, target, res, curr, index, seen) {
		if (target === 0) {
			res.push([...curr]);
		} else if (target < 0) {
			return;
		} else {
			for (let i = index; i < nums.length; i++) {
				if (seen[i]) continue;
				if (i > index && nums[i] === nums[i - 1]) continue;
				curr.push(nums[i]);
				seen[i] = true;
				this.#singleCombination(nums, target - nums[i], res, curr, i + 1, seen);
				curr.pop();
				seen[i] = false;
			}
		}
	}
}

const candidates = [1, 2, 3, 4, 5];
// const candidates = [2, 1, 1, 5];
const target = 7;
const sol = new Solution();
console.log(sol.combinationSum2(candidates, target));
