var reverseOnlyLetters = function (s) {
	let l = 0,
		r = s.length - 1;
	const res = new Array(s.length).fill(null);
	while (l <= r) {
		if (!s[l].match(/[a-zA-Z ]+/)) {
			res[l] = s[l++];
		} else if (!s[r].match(/[a-zA-Z ]+/)) {
			res[r] = s[r--];
		} else {
			res[l] = s[r];
			res[r--] = s[l++];
		}
	}
	//	if (l === r) res[l] = s[l];
	return res.join('');
};

const s = 'a-bC-dEf-ghIj';
console.log(reverseOnlyLetters(s));
