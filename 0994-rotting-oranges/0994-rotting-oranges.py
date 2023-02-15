class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count,fresh_org = 0 , 0
        queue = []
        row,col = len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_org  += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        print(queue,fresh_org)
        while queue and fresh_org > 0:
            
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                
                if  0 <= c-1 < col and grid[r][c-1] == 1:
                    # print(grid[r][c-1])                
                    queue.append([r,c-1])
                    grid[r][c-1] = 2
                    fresh_org -= 1
                if 0 <= c+1 < col and grid[r][c+1] == 1:
                    
                    queue.append([r,c+1])
                    grid[r][c+1] = 2 
                    fresh_org -= 1
                if 0 <= r-1 < row and grid[r-1][c] == 1:
                    queue.append([r - 1,c])
                    grid[r - 1][c] = 2
                    fresh_org -= 1
                if 0 <= r+1 < row and grid[r+1][c] == 1:
                    # print(grid[r+1][c])
                    queue.append([r + 1,c])
                    print("p")
                    grid[r + 1][c] = 2
                    fresh_org -= 1
            count += 1
            # print(queue,fresh_org)
        
        if fresh_org != 0:
            return -1
        else:
            return count
        
                    