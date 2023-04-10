class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = grid
        row_bound = len(grid) - 1
        col_bound = len(grid[0]) - 1
        
        for row in range(row_bound,-1,-1):
            for col in range(col_bound,-1,-1):
                   
                # 1 case - can go right and down
                if col + 1 <= col_bound and row + 1 <= row_bound:
                    val = min(res[row][col + 1],res[row + 1][col])
                    res[row][col] = grid[row][col] + val
                    
                # 2 case - can only go right
                elif col + 1 <= col_bound:
                    res[row][col] = grid[row][col] + grid[row][col + 1]
                # 3 case - can only go down
                elif row + 1 <= row_bound:
                    res[row][col] = grid[row][col] + grid[row + 1][col]
                else:
                    continue #Base Case                
        return res[0][0]
                
            