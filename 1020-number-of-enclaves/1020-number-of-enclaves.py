class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid :
            return
        visited = set()
        
        def dfs(x,y):
            visited.add((x,y))
            
            for x,y in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y]:
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visited and (i == 0 or j == 0 or i == len(grid) - 1 or  j == len(grid[0]) - 1):
                    dfs(i,j)
        # print(visited)
        
        count_res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j]:
                    count_res += 1
        return count_res