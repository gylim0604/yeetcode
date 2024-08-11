class Solution {
	/**
	 * @param {number} target
	 * @param {number[]} position
	 * @param {number[]} speed
	 * @return {number}
	 */
	carFleet(target, position, speed) {
		let res = 0;
		let temp = [];
		for (let i = 0; i < position.length; i++) {
			temp.push({
				speed: speed[i],
				position: position[i],
				turns: (target - position[i]) / speed[i],
			});
		}
		temp.sort((a, b) => b.position - a.position);
		for (let i = 0; i < temp.length; i++) {
			if (i >= 1 && temp[i].turns <= temp[i - 1].turns) {
				temp[i].turns = temp[i - 1].turns;
			} else {
				res++;
			}
		}
		return res;
	}
}

const target = 10,
	position = [4, 1, 0, 7],
	speed = [3, 2, 10, 1];
const sol = new Solution();
console.log(sol.carFleet(target, position, speed));
