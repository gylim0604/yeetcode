class Solution {
	/**
	 * @param {string} s
	 * @return {string}
	 */
	longestPalindrome(s) {
		return this.#expandAtCenter(s);
	}

	#expandAtCenter(s) {
		if (!s || s.length === 0) return '';
		let l = 0,
			r = 0;
		for (let i = 0; i < s.length - 1; i++) {
			const odd = this.#expand(s, i, i);
			const even = this.#expand(s, i, i + 1);

			const maxLen = Math.max(odd, even);

			if (maxLen > r - l) {
				l = i - Math.floor((maxLen - 1) / 2);
				r = i + Math.floor(maxLen / 2);
			}
		}
		return s.slice(l, r + 1);
	}

	#expand(s, l, r) {
		if (s.length === 0 || l > r) return 0;
		while (l >= 0 && r < s.length && s[l] === s[r]) {
			l--;
			r++;
		}
		return r - l - 1;
	}
	// #findPalindrome(s, found) {
	// 	if (found[s]) return s;

	// 	if (this.#isPalindrome(s)) {
	// 		found[s] = true;
	// 		return s;
	// 	} else {
	// 		found[s] = false;
	// 	}
	// 	const curr = this.#findPalindrome(s.slice(0, s.length - 1), found);
	// 	const curr2 = this.#findPalindrome(s.slice(1), found);
	// 	return curr.length > curr2.length ? curr : curr2;
	// }

	// #isPalindrome(s) {
	// 	if (s.length === 1) {
	// 		return true;
	// 	}
	// 	let l = 0,
	// 		r = s.length - 1;
	// 	while (l < r) {
	// 		if (s[l++] !== s[r--]) return false;
	// 	}
	// 	return true;
	// }
}

const str = 'abbc';
const sol = new Solution();
console.log(sol.longestPalindrome(str));
