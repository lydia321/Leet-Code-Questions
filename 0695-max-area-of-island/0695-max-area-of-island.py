class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return
        res = 0
        visited = set()
        
        def dfs(x,y):
            curr_area = 1
            visited.add((x,y))
            
            for x,y in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y]:
                    curr_area += dfs(x,y)
            return curr_area
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visited:
                    curr_area = dfs(i,j)
                    res = max(res,curr_area)
        return res