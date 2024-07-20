const shortestToChar = function (s, c) {
	let res = new Array(s.length).fill(null);
	let prev = null;
	for (let l = 0; l < s.length; l++) {
		if (s[l] === c) prev = l;
		if (prev !== null) {
			res[l] = l - prev;
		}
	}
	prev = null;
	for (let r = s.length - 1; r >= 0; r--) {
		if (s[r] === c) prev = r;
		if (prev !== null) {
			res[r] = Math.min(res[r] ?? Infinity, prev - r);
		}
	}
	return res;
};

const s = 'aabaa',
	c = 'b';
console.log(shortestToChar(s, c));
