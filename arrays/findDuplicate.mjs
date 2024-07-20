class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number}
	 */
	findDuplicate(nums) {
		let slow = 0;
		let fast = 0;
		while (true) {
			slow = nums[slow];
			fast = nums[nums[fast]];

			if (slow === fast) {
				break;
			}
		}
		console.log(slow);
		let ptr1 = 0;
		let ptr2 = slow;
		while (ptr1 !== ptr2) {
			console.log(ptr1, ptr2);
			ptr2 = nums[ptr2];
			ptr1 = nums[ptr1];
		}
		return ptr1;
	}
}

const nums = [1, 3, 6, 5, 2, 4, 7, 8, 9, 2];
const sol = new Solution();
sol.findDuplicate(nums);
