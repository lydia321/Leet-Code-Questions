class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(i, j):
            for c in range(9):
                if c != j:
                    if board[i][j] == board[i][c]:
                        return False
                    
            return True

        def checkCol(i, j):
            for r in range(9):
                if r != i:
                    if board[i][j] == board[r][j]:
                        return False

            return True    

        def checkBox(i, j):
            if i in (0, 1, 2):  
                rs, re = 0, 2
            elif i in (3, 4, 5):
                rs, re = 3, 5
            else:
                rs, re = 6, 8

            if j in (0, 1, 2):  
                cs, ce = 0, 2
            elif j in (3, 4, 5):
                cs, ce =3, 5
            else:
                cs, ce = 6, 8    

            for r in range(rs, re + 1):
                for c in range(cs, ce + 1):
                    if i != r or j != c:
                        if board[i][j] == board[r][c]:
                            return False
            return True    

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if checkRow(i, j) and checkCol(i, j) and checkBox(i, j):
                        continue
                    return False

        return True