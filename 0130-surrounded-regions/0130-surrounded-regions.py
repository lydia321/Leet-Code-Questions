class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        if not grid:
            return
        visited = set()
        
        def dfs(x,y):
            visited.add((x,y))
            
            for x,y in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if x in range(len(grid)) and y in range(len(grid[0])) and (x,y) not in visited and grid[x][y] == "O":
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "O" and (i,j) not in visited and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    dfs(i,j)
        # print(visited)
                     
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j] == "O":
                    grid[i][j] = "X"
                
        """
        Do not return anything, modify board in-place instead.
        """
        