class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToTurn = []
        colsToTurn = []
        
        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if matrix[row][i] == 0:
                    rowsToTurn.append(row)
                    colsToTurn.append(i)
        # print(rowsToTurn,colsToTurn)
        
        for i in rowsToTurn:
            for r in range(len(matrix[i])):
                matrix[i][r] = 0
        
        for c in range(len(matrix)):
            for j in colsToTurn:
                matrix[c][j] = 0
                
                
                           
        """
        Do not return anything, modify matrix in-place instead.
        """
