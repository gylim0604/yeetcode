class Solution {
	/**
	 * @param {string} s
	 * @return {string}
	 */
	longestPalindrome(s) {
		// return this.#expandAtCenter(s);
		return this.#dp(s);
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

	#dp(s) {
		let start = 0,
			maxLen = 1;
		// dp is a 2d array representing whether dp[i...j] is a palindrome
		const dp = [...new Array(s.length + 1)].map((_) => new Array(s.length + 1).fill(false));
		// Fill up value for single character
		for (let i = 0; i < s.length; i++) {
			dp[i] = [];
			dp[i][i] = true;
		}
		// fill up length 2 strings
		for (let i = 0; i < s.length - 1; i++) {
			if (s[i] === s[i + 1]) {
				dp[i][i + 1] = true;
				start = i;
				maxLen = 2;
			}
		}

		for (let len = 3; len < s.length + 1; len++) {
			for (let i = 0; i < s.length - len + 1; i++) {
				const j = i + len - 1;
				if (s[i] === s[j] && dp[i + 1][j - 1]) {
					dp[i][j] = true;
					if (len > maxLen) {
						start = i;
						maxLen = len;
					}
				}
			}
		}
		return s.slice(start, start + maxLen);
	}
}

const str = 'abcba';
const sol = new Solution();
console.log(sol.longestPalindrome(str));
