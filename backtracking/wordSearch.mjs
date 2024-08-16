class Solution {
	/**
	 * @param {character[][]} board
	 * @param {string} word
	 * @return {boolean}
	 */
	exist(board, word) {
		return this.#search(board, word, 0, 0, 0);
	}

	#search(board, word, row, col, index) {
		if (index === word.length) {
			return true;
		}
		if (col >= board[0].length || row >= board.length) {
			return false;
		}
		if (board[row][col] === word[index]) {
			index++;
		} else {
			index = 0;
		}
		return this.#search(board, word, row, col + 1, index) || this.#search(board, word, row + 1, col, index);
	}
}

const board = [
	['A', 'B', 'C', 'D'],
	['S', 'A', 'A', 'T'],
	['A', 'C', 'A', 'E'],
];
// const board = [['A', 'B', 'C', 'A', 'T']];
const word = 'CAT';
// const board = [
// 	['A', 'B'],
// 	['A', 'A'],
// ];
// // const word = 'AA';
// const word = 'ABC';
const sol = new Solution();
console.log(sol.exist(board, word));
