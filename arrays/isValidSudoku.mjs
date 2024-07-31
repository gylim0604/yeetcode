class Solution {
	/**
	 * @param {character[][]} board
	 * @return {boolean}
	 */
	isValidSudoku(board) {
		let height = board.length;
		let width = board[0].length;
		let rowArr = [];
		let colArr = [];
		let subGrid = [];
		for (let i = 0; i < height; i++) {
			rowArr = [];
			colArr = [];
			subGrid = [];
			for (let j = 0; j < width; j++) {
				rowArr.push(board[i][j]);
				colArr.push(board[j][i]);
				const index = Math.floor(i / 3) * 3 + Math.floor(j / 3);
				const index2 = (i % 3) * 3 + (j % 3);
				subGrid.push(board[index][index2]);
			}
			if (this.#isValid(rowArr) || this.#isValid(colArr) || this.#isValid(subGrid)) return false;
		}

		return true;
	}

	#isValid(arr) {
		let set = new Set();
		for (let el of arr) {
			if (el === '.') continue;
			if (set.has(el)) return true;
			set.add(el);
		}
		return false;
	}
}
const board = [
	['1', '2', '.', '.', '3', '.', '.', '.', '.'],
	['4', '.', '.', '5', '.', '.', '.', '.', '.'],
	['.', '9', '8', '.', '.', '.', '.', '.', '3'],
	['5', '.', '.', '.', '6', '.', '.', '.', '4'],
	['.', '.', '.', '8', '.', '3', '.', '.', '5'],
	['7', '.', '.', '.', '2', '.', '.', '.', '6'],
	['.', '.', '.', '.', '.', '.', '2', '.', '.'],
	['.', '.', '.', '4', '1', '9', '.', '.', '8'],
	['.', '.', '.', '.', '8', '.', '.', '7', '9'],
];
const sol = new Solution();
console.log(sol.isValidSudoku(board));
