var findTheArrayConcVal = function (nums) {
	let l = 0,
		r = nums.length - 1;
	let res = 0;
	while (l < r) {
		const sum = nums[l++] + '' + nums[r--];
		res += Number(sum);
	}
	if (l === r) res += nums[l];
	return res;
};

const nums = [7, 52, 2, 4];
console.log(findTheArrayConcVal(nums));
