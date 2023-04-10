class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        res = matrix
        row_bound = len(matrix) - 1
        col_bound = len(matrix[0]) - 1
        
        for row in range(1,row_bound + 1):
            for col in range(col_bound + 1):
    
                if col - 1 < 0:
                    val =  min((res[row - 1][col]),(res[row - 1][col + 1]))
                    res[row][col] += val
                elif col + 1 > col_bound:
                    val =  min((res[row - 1][col]),(res[row - 1][col - 1]))
                    res[row][col] += val
                else:
                    val =  min((res[row - 1][col]),(res[row - 1][col + 1]),(res[row - 1][col - 1]))
                    res[row][col] += val
      
        return min(res[-1])
                
      