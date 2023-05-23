class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        seen = set() 
        row_bound = len(grid) 
        col_bound = len(grid[0])
        
        def dfs(row,col):
            nonlocal mr
            nonlocal mc
            seen.add((row,col))
            if (row + 1,col) not in seen and ((row + 1 ) < row_bound) and grid[row + 1][col] == 1:
                mr = max(mr,row + 1)
                dfs(row + 1,col)
            if (row - 1,col) not in seen and ((row - 1 ) >= 0) and grid[row - 1][col] == 1:
                mr = max(mr,row - 1)
                dfs(row - 1,col)
            if (row,col- 1) not in seen and ((col - 1 ) >= 0) and grid[row][col - 1] == 1:
                mc = max(mc,col - 1)
                dfs(row,col - 1)
            if (row,col + 1) not in seen and ((col + 1 ) < col_bound) and grid[row][col + 1] == 1:
                mc = max(mc,col + 1)
                dfs(row,col + 1)
        res = []       
        for row in range(len(grid)):
            
            for col in range(len(grid[0])):
                curr = []
                if (row,col) not in seen and grid[row][col] == 1:
    
                    curr.append(row)
                    curr.append(col)
                    mr,mc = row,col
                    dfs(row,col)
                    curr.append(mr)
                    curr.append(mc)
                if curr: res.append(curr)
                   
       
        return res