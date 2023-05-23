class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() 
        row_bound = len(grid) 
        col_bound = len(grid[0])
        
        def dfs(row,col):
            seen.add((row,col))
            if (row + 1,col) not in seen and ((row + 1 ) < row_bound) and grid[row + 1][col] =='1':
                dfs(row + 1,col)
            if (row - 1,col) not in seen and ((row - 1 ) >= 0) and grid[row - 1][col] =='1':
                dfs(row - 1,col)
            if (row,col- 1) not in seen and ((col - 1 ) >= 0) and grid[row][col - 1] =='1':
                dfs(row,col - 1)
            if (row,col + 1) not in seen and ((col + 1 ) < col_bound) and grid[row][col + 1] == '1':
                dfs(row,col + 1)
        res = 0        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in seen and grid[row][col] == '1':
                    res += 1
                    dfs(row,col)
                    # print(res,seen)
       
        return res
        
       
      