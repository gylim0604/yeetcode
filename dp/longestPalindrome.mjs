class Solution {
	/**
	 * @param {string} s
	 * @return {string}
	 */
	longestPalindrome(s) {
		return this.#findPalindrome(s);
	}

	#findPalindrome(s) {
		if (s.length === 1) {
			return s;
		}
		if (this.#isPalindrome(s)) return s;
		const curr = this.#findPalindrome(s.slice(0, s.length - 1));
		const curr2 = this.#findPalindrome(s.slice(1));
		return curr.length > curr2.length ? curr : curr2;
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

const str = 'abbc';
const sol = new Solution();
console.log(sol.longestPalindrome(str));
