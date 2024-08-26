class Solution {
	/**
	 * @param {string} s
	 * @return {string}
	 */
	longestPalindrome(s) {
		const found = {};
		return this.#findPalindrome(s, found);
	}

	#findPalindrome(s, found) {
		if (found[s]) return s;

		if (this.#isPalindrome(s)) {
			found[s] = true;
			return s;
		} else {
			found[s] = false;
		}
		const curr = this.#findPalindrome(s.slice(0, s.length - 1), found);
		const curr2 = this.#findPalindrome(s.slice(1), found);
		return curr.length > curr2.length ? curr : curr2;
	}

	#isPalindrome(s) {
		if (s.length === 1) {
			return true;
		}
		let l = 0,
			r = s.length - 1;
		while (l < r) {
			if (s[l++] !== s[r--]) return false;
		}
		return true;
	}
}

const str = 'aabbccddeeffgghh';
const sol = new Solution();
console.log(sol.longestPalindrome(str));
