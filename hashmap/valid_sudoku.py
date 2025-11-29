"""
Valid Sudoku
-----------
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
-----------
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
-----------
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:
-----------
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = 9

        def has_duplicates(elements):
            seen = set()
            for element in elements:
                if element != '.' and element in seen:
                    return True
                seen.add(element)
            return False

        # Check each row for duplicates
        for row in range(board_size):
            if has_duplicates(board[row]):
                return False

        # Check each column for duplicates
        for column in range(board_size):
            if has_duplicates([board[row][column] for row in range(board_size)]):
                return False

        # Check each 3x3 sub-box for duplicates
        # Ensures each sub-box has unique values
        for box_row in range(0, board_size, 3):
            for box_column in range(0, board_size, 3):
                elements_in_subgrid = [
                    board[row][column]
                    for row in range(box_row, box_row + 3)
                    for column in range(box_column, box_column + 3)
                ]
                if has_duplicates(elements_in_subgrid):
                    return False

        return True