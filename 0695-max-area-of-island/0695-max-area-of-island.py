class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        res_area = 0
        
        def dfs(x,y):
            visited.add((x,y))
            curr_count = 1
            for x,y in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y]:
                    curr_count += dfs(x,y)
            return curr_count
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visited:
                    curr_count = dfs(i,j)
                    res_area = max(res_area,curr_count)
        return res_area