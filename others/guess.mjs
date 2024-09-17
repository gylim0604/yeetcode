var pick = 6;

var guessNumber = function (n) {
	let left = 0,
		right = n;
	let mid = Math.floor((left + right) / 2);
	let res = guess(mid);
	while (res !== 0) {
		if (res === 1) {
			left = mid;
			mid = Math.floor((left + right) / 2);
		} else if (res === -1) {
			right = mid;
			mid = Math.floor((left + right) / 2);
		}
		res = guess(mid);
	}
	return mid;
};

const guess = function (n) {
	if (n === pick) return 0;
	if (n > pick) return -1;
	if (n < pick) return 1;
};

console.log(guessNumber(10));
