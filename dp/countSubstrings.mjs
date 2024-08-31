class Solution {
	/**
	 * @param {string} s
	 * @return {number}
	 */
	countSubstrings(s) {
		let count = 0;
		// check how many palindromes can we get from each char as center
		for (let i = 0; i < s.length; i++) {
			count += this.#expand(s, i, i);
			count += this.#expand(s, i, i + 1);
		}
		return count;
	}

	#expand(s, l, r) {
		if (s.length === 0 || l > r) return 0;
		let count = 0;
		while (l >= 0 && r < s.length && s[l] === s[r]) {
			count++;
			l--;
			r++;
		}
		return count;
	}
}

const s = 'aaa';
const sol = new Solution();
console.log(sol.countSubstrings(s));
