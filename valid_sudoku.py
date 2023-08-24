#qus:- Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#1.Each row must contain the digits 1-9 without repetition.
#2.Each column must contain the digits 1-9 without repetition.
#.Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if ("row" + str(i) + board[i][j]) in seen or ("column" + str(j) + board[i][j]) in seen:
                        return False
                    if ("box" + str(i // 3 * 3 + j // 3) + board[i][j]) in seen:
                        return False
                    
                    seen.add("row" + str(i) + board[i][j])
                    seen.add("column" + str(j) + board[i][j])
                    seen.add("box" + str(i // 3 * 3 + j // 3) + board[i][j])
        
        return True
 