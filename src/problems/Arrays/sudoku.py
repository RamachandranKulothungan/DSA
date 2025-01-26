"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def get_box_index(x, y):
        if x <= 2:
            if y <= 2: return 0
            elif y <= 5: return 1
            elif y <=8: return 2
        elif x <= 5:
            if y <= 2: return 3
            elif y <= 5: return 4
            elif y <=8: return 5
        elif x <= 8:
            if y <= 2: return 6
            elif y <= 5: return 7
            elif y <=8: return 8

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for x in range(9)]
        col_sets = [set() for x in range(9)]
        box_sets = [set() for x in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_sets[i]:
                    print(f"row {i} is invalid with {board[i][j]}: {row_sets[i]}")
                    return False
                if board[i][j] in col_sets[j]:
                    print(f"col {j} is invalid with {board[i][j]}: {col_sets[j]}")
                    return False
                box_index = get_box_index(i, j)
                if board[i][j] in box_sets[box_index]:
                    print(f"box {box_index} is invalid with {board[i][j]}: {box_sets[box_index]}")
                    return False
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                box_sets[box_index].add(board[i][j])
        return True