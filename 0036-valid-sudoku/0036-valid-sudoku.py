class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row,col):
            for each_col in range(9):
                if each_col != col: #each col except for the col passed
                    if board[row][col] == board[row][each_col]:
                        return False
            return True

        def checkCol(row,col):
            for each_row in range(9):
                if each_row != row: # each row except the one passed
                    if board[row][col] == board[each_row][col]:
                        
                        return False
            return True

        def checkBox(row,col):
            if row in (0, 1, 2):
                row_start,row_end = 0, 2
            elif row in (3, 4, 5):
                row_start , row_end = 3, 5
            else:
                row_start, row_end = 6, 8

            if col in (0, 1, 2):
                col_start, col_end = 0 ,2
            elif col in (3, 4, 5):
                col_start, col_end = 3, 5
            else:
                col_start, col_end = 6, 8

                
            for r in range(row_start, row_end + 1):
                
                for c in range(col_start, col_end + 1):
                    
                    if row != r or col != c:
                        
                        if board[row][col] == board[r][c]:
                            
                            return False
                                    
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if checkRow(row,col) and checkCol(row,col) and checkBox(row,col):
                        continue
                    return False
        return True
