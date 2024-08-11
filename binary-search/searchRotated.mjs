class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	search(nums, target) {
		let l = 0,
			r = nums.length - 1;
		while (l <= r) {
			const mid = l + Math.floor((r - l) / 2);
			const midNum = nums[mid];
			const leftNum = nums[l];
			const rightNum = nums[r];
			if (midNum === target) {
				return mid;
			}
			if (midNum >= leftNum) {
				// left is sorted
				if (leftNum > target || target > midNum) {
					// target exist in other portion
					// left is larger than target [left, ..., mid, ...target]
					// mid is smaller than target [left,...mid...target]
					l = mid + 1;
				} else {
					// target is within left portion
					r = mid - 1;
				}
			} else {
				if (target < midNum || target > rightNum) {
					r = mid - 1;
				} else {
					l = mid + 1;
				}
			}
		}
		return -1;
	}
}
const nums = [3, 4, 5, 6, 1, 2];
// const nums = [5, 1, 3];
const target = 6;
const sol = new Solution();
console.log(sol.search(nums, target));
