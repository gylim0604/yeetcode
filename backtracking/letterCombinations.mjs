class Solution {
	/**
	 * @param {string} digits
	 * @return {string[]}
	 */
	#dict = {
		2: ['a', 'b', 'c'],
		3: ['d', 'e', 'f'],
		4: ['g', 'h', 'i'],
		5: ['j', 'k', 'l'],
		6: ['m', 'n', 'o'],
		7: ['p', 'q', 'r', 's'],
		8: ['t', 'u', 'v'],
		9: ['w', 'x', 'y', 'z'],
	};
	/**
	 * @param {string} digits
	 * @return {string[]}
	 */
	letterCombinations(digits) {
		const res = [];
		const curr = [];
		const arr = digits.split('');
		for (let i = 0; i < arr.length; i++) {
			// get individual keys
			const prefixArr = this.#dict[arr[i]];
			for (let j = 0; j < prefixArr.length; j++) {
				this.#dfs(arr, res, [prefixArr[j]], i + 1);
			}
		}
		return res;
	}

	#dfs(digits, res, curr, index) {
		if (curr.length === digits.length) {
			res.push(curr.join(''));
			return;
		}
		for (let i = index; i < digits.length; i++) {
			const chars = this.#dict[digits[i]];
			for (let j = 0; j < chars.length; j++) {
				curr.push(chars[j]);
				this.#dfs(digits, res, curr, i + 1);
				curr.pop();
			}
		}
	}
}

const digits = '34';
const sol = new Solution();
console.log(sol.letterCombinations(digits));
