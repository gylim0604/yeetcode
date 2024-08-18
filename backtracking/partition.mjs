class Solution {
	/**
	 * @param {string} s
	 * @return {string[][]}
	 */
	partition(s) {
		const res = [];
		const curr = [];
		this.#singlePartition(s, res, curr, 0);
		return res;
	}

	#singlePartition(s, res, curr, index) {
		if (index === s.length) {
			res.push([...curr]);
			return;
		}
		for (let i = index; i < s.length; i++) {
			const currStr = s.substring(index, i + 1);
			if (this.#isPalindrome(currStr)) {
				curr.push(currStr);
				this.#singlePartition(s, res, curr, i + 1);
				curr.pop();
			}
		}
	}

	#isPalindrome(s) {
		let l = 0,
			r = s.length - 1;
		while (l < r) {
			if (s[l++] !== s[r--]) return false;
		}
		return true;
	}
}

const s = 'abbab';
const sol = new Solution();
console.log(sol.partition(s));
