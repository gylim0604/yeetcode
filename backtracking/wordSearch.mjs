class Solution {
	/**
	 * @param {character[][]} board
	 * @param {string} word
	 * @return {boolean}
	 */
	exist(board, word) {
		for (let i = 0; i < board.length; i++) {
			for (let j = 0; j < board[i].length; j++) {
				if (this.#search(board, word, i, j, 0)) {
					return true;
				}
			}
		}
		return false;
	}

	#search(board, word, row, col, index) {
		if (index === word.length) {
			return true;
		}
		if (col < 0 || row < 0 || col >= board[0].length || row >= board.length || board[row][col] !== word[index]) {
			return false;
		}
		const temp = board[row][col];
		board[row][col] = '#';
		const found = this.#search(board, word, row, col + 1, index + 1) || this.#search(board, word, row + 1, col, index + 1) || this.#search(board, word, row, col - 1, index + 1) || this.#search(board, word, row - 1, col, index + 1);
		board[row][col] = temp;
		return found;
	}
}

const board = [
	['A', 'B', 'C', 'D'],
	['S', 'A', 'A', 'T'],
	['A', 'C', 'A', 'E'],
];
const word = 'CAAC';

// const word = 'CAT';
// const word = 'ABC';
const sol = new Solution();
console.log(sol.exist(board, word));
