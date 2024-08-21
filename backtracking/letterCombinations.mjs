class Solution {
	#dict = {
		2: 'abc',
		3: 'def',
		4: 'ghi',
		5: 'jkl',
		6: 'mno',
		7: 'qprs',
		8: 'tuv',
		9: 'wxyz',
	};
	/**
	 * @param {string} digits
	 * @return {string[]}
	 */
	letterCombinations(digits) {
		let res = [];
		if (digits) {
			this.#combine(digits, res, '', 0);
		}
		return res;
	}

	#combine(digits, res, curr, idx) {
		if (curr.length === digits.length) {
			res.push(curr);
			return;
		}
		// Go through each
		for (const char of this.#dict[digits[idx]]) {
			this.#combine(digits, res, curr + char, idx + 1);
		}
	}
}

const digits = '34';
const sol = new Solution();
console.log(sol.letterCombinations(digits));
