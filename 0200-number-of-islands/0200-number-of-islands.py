class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        visited = set()
        islands = 0
        
        def dfs(x,y):
            visited.add((x,y))
            
            for x,y in [x,y+1], [x,y-1], [x+1,y], [x-1,y]:
                if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited  and grid[x][y] == '1':
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
        return islands
    